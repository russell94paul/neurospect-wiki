"""Assemble the Lanes page: graph JSON + a dependency figure whose geometry comes
from the edge counts, not from eyeballing."""
import io, json, pathlib

W = pathlib.Path(r'C:\Users\PaulRussell\repos\neurospect-wiki')
SCR = pathlib.Path(__file__).parent
G = json.load(io.open(W / 'processes/distributed-workflow/flow-graph.json', encoding='utf-8'))

# order by in-degree: the trackers others depend on rise to the top
indeg = {t['file']: 0 for t in G}
for t in G:
    for l in t['links']:
        if l in indeg:
            indeg[l] += 1
order = sorted(G, key=lambda t: (-indeg[t['file']], t['file']))
idx = {t['file']: i for i, t in enumerate(order)}

ROW, PADT, LEFT, W_ = 26, 26, 250, 1000
H = PADT + ROW * len(order) + 18
p = [f'<svg class="dep" viewBox="0 0 {W_} {H}" role="img" xmlns="http://www.w3.org/2000/svg" '
     f'aria-label="Dependency graph of {len(order)} Neurospect workstream trackers, ordered by how '
     f'many other trackers cite them. Live lanes are outlined.">']

# edges first, behind the nodes
for t in G:
    y0 = PADT + idx[t['file']] * ROW
    for l in t['links']:
        if l not in idx:
            continue
        y1 = PADT + idx[l] * ROW
        # bow right, proportional to the distance travelled — a long dependency looks long
        bow = LEFT + 30 + abs(y1 - y0) * 1.15
        p.append(f'<path class="ed" d="M {LEFT} {y0} C {bow:.0f} {y0}, {bow:.0f} {y1}, {LEFT} {y1}"/>')

for t in order:
    i = idx[t['file']]
    y = PADT + i * ROW
    isl = any(ph['status'] == 'ACTIVE' for ph in t['phases'])
    cls = 'nd' + (' live' if isl else '') + (' closed' if t['closed'] else '')
    p.append(f'<circle class="{cls}" cx="{LEFT}" cy="{y}" r="5"/>')
    name = t['file'].replace('.md', '')
    p.append(f'<text class="lbl{" live" if isl else ""}" x="{LEFT-12}" y="{y+3.5}" '
             f'text-anchor="end">{name}</text>')
    n = indeg[t['file']]
    p.append(f'<text x="{LEFT+22}" y="{y+3.5}">{n} in · {len(t["links"])} out'
             f'{" · LIVE" if isl else ""}{" · closed" if t["closed"] else ""}</text>')
p.append('</svg>')

src = io.open(SCR / 'flow.src.html', encoding='utf-8').read()
src = src.replace('__GRAPH__', json.dumps(G, separators=(',', ':')))
src = src.replace('__DEPS__', '\n'.join(p))
for tok in ('__GRAPH__', '__DEPS__'):
    assert tok not in src, tok
out = SCR / 'flow.html'
out.write_text(src, encoding='utf-8')

live = [ph['phase'] for t in G for ph in t['phases'] if ph['status'] == 'ACTIVE']
print(f'wrote {out} ({len(src)/1024:.0f} KB)')
print(f'  {len(G)} trackers, {sum(len(t["phases"]) for t in G)} phases, '
      f'{sum(len(t["links"]) for t in G)} edges')
print(f'  live: {", ".join(live)}')
print(f'  nodes drawn: {sum(1 for x in p if "circle" in x)} (expect {len(order)})')
