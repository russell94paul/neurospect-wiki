"""Extract the workstream dependency + gate graph from the tracker files.

Parsed, never transcribed — a graph typed by hand has already drifted.

Two deliberate choices:
  * Phase STATUS comes from the boot-prompt heading's own marker.
  * Gate REASON comes from that same heading, not from body prose. Prose saying
    "blocked on ..." is discussion, not status, and produced pure noise.
"""
from __future__ import annotations

import glob
import io
import json
import pathlib
import re
from collections import Counter

W = pathlib.Path(__file__).resolve().parents[1]
ACTIVE = W / 'processes/distributed-workflow/active'

STATUS = [                                    # first match wins; order is precedence
    (r'⏭\s*ACTIVE', 'ACTIVE'),
    (r'✅\s*(?:RUN|EXECUTED|CLOSED)', 'RUN'),
    (r'❌|NEVER RUN', 'NEVER-RUN'),
    (r'SUPERSEDED', 'SUPERSEDED'),
    (r'➡️|MOVED', 'MOVED'),
    (r'⏸?\s*GATED', 'GATED'),
    (r'⏸\s*NEXT|⏸', 'NEXT'),
    (r'PART-RUN', 'PART-RUN'),
]
GATE_RE = re.compile(r'(?:GATED|blocked)\s+on\s+(.{3,70})', re.I)
LINK_RE = re.compile(r'\[\[processes/distributed-workflow/active/([a-z0-9-]+)\]\]')


def cls(g: str) -> str:
    gl = g.lower()
    if 'paul' in gl or 'human' in gl:
        return 'HUMAN'
    if 'instrument' in gl:
        return 'INSTRUMENT'
    if re.search(r'session|phase|\bs1|\bb[1-4]\b', gl):
        return 'WORK'
    return 'OTHER'


def status_of(line: str) -> str:
    for pat, name in STATUS:
        if re.search(pat, line):
            return name
    return 'UNMARKED'


def parse(path: pathlib.Path) -> dict:
    txt = io.open(path, encoding='utf-8').read()
    head = txt[:4000]
    phases = []
    for i, ln in enumerate(txt.split('\n')):
        m = re.match(r'^## (?:Next Session )?Boot Prompt(?: Archive)?\s*[—-]?\s*\(?(.*)$', ln)
        if not m:
            continue
        rest = m.group(1)
        pm = re.search(r'(Phase\s+[A-Za-z0-9._-]+|Skill authoring)', rest)
        gm = GATE_RE.search(ln)
        on = re.sub(r'[*`]', '', gm.group(1)).strip(' .)') if gm else ''
        phases.append({
            'phase': (pm.group(1) if pm else rest.split('—')[0].strip(' ()'))[:46],
            'title': re.sub(r'\s+', ' ', rest.split('—')[1].strip())[:70] if '—' in rest else '',
            'status': status_of(ln),
            'on': on,
            'kind': cls(on) if on else '',
            'line': i + 1,
        })
    t = re.search(r'^# (.+)$', txt, re.M)
    u = re.search(r'^updated:\s*(\S+)', head, re.M)
    return {
        'file': path.name,
        'title': t.group(1) if t else path.stem,
        'updated': u.group(1) if u else '?',
        'closed': bool(re.search(r'WORKSTREAM CLOSED', head, re.I)),
        'links': sorted({m.group(1) + '.md' for m in LINK_RE.finditer(txt)} - {path.name}),
        'phases': phases,
        'words': len(txt.split()),
    }


def main() -> None:
    out = [parse(pathlib.Path(p)) for p in sorted(glob.glob(str(ACTIVE / '*.md')))]
    p = W / 'processes/distributed-workflow/flow-graph.json'
    p.write_text(json.dumps(out, indent=1), encoding='utf-8')

    print(f'{len(out)} trackers - {sum(len(t["phases"]) for t in out)} phases - '
          f'{sum(t["words"] for t in out):,} words')
    print('\nACTIVE lanes:')
    for t in out:
        for ph in t['phases']:
            if ph['status'] == 'ACTIVE':
                print(f'  {t["file"]:28} {ph["phase"]}')
    print('\ngates, from the heading:')
    for t in out:
        for ph in t['phases']:
            if ph['on']:
                print(f'  {t["file"]:26} {ph["phase"]:14} [{ph["status"]:10}] <- '
                      f'{ph["on"][:50]} ({ph["kind"]})')
    e = 0
    print('\ncross-tracker edges:')
    for t in out:
        for l in t['links']:
            print(f'  {t["file"]:28} -> {l}')
            e += 1
    print(f'  ({e} edges)')
    print('\nphase states:',
          dict(Counter(ph['status'] for t in out for ph in t['phases']).most_common()))
    un = [(t['file'], ph['phase']) for t in out for ph in t['phases'] if ph['status'] == 'UNMARKED']
    print(f'\nphases with NO status marker ({len(un)}) - a lane nobody can see the state of:')
    for f, ph in un:
        print(f'  {f:28} {ph}')
    print(f'\nwrote {p}')


if __name__ == '__main__':
    main()
