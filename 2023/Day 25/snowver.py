"""
Fortunately, someone left a wiring diagram (your puzzle input) that shows how the components are connected. For example:

jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
Each line shows the name of a component, a colon, and then a list of other components to which that component is connected. 
Connections aren't directional; abc: xyz and xyz: abc both represent the same configuration. Each connection between two 
components is represented only once, so some components might only ever appear on the left or right side of a colon.

In this example, if you disconnect the wire between hfx/pzl, the wire between bvb/cmg, and the wire between nvd/jqt, 
you will divide the components into two separate, disconnected groups:

9 components: cmg, frs, lhk, lsr, nvd, pzl, qnr, rsh, and rzs.
6 components: bvb, hfx, jqt, ntq, rhn, and xhk.
Multiplying the sizes of these groups together produces 54.

Find the three wires you need to disconnect in order to divide the components into two separate groups. What do you get 
if you multiply the sizes of these two groups together?

reference: https://www.reddit.com/r/adventofcode/comments/18qbsxs/comment/ketzp94/
"""

import collections as C


G = C.defaultdict(set)

for line in open('data.txt'):
    u, *vs = line.replace(':','').split()
    for v in vs: G[u].add(v); G[v].add(u)


S = set(G)

count = lambda v: len(G[v]-S)

while sum(map(count, S)) != 3:
    S.remove(max(S, key=count))

print(len(S) * len(set(G)-S))
