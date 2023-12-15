"""

reference:
https://www.reddit.com/r/adventofcode/comments/18df7px/comment/kcguu6a

After examining the maps for a bit, two nodes stick out: AAA and ZZZ. 
You feel like AAA is where you are now, and you have to follow the left/right instructions until you reach ZZZ.

This format defines each node of the network individually. For example:

RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
Starting with AAA, you need to look up the next element based on the next left/right instruction in your input. 
In this example, start with AAA and go right (R) by choosing the right element of AAA, CCC. 
Then, L means to choose the left element of CCC, ZZZ. By following the left/right instructions, you reach ZZZ in 2 steps.

Of course, you might not find ZZZ right away. If you run out of left/right instructions, 
repeat the whole sequence of instructions as necessary: RL really means RLRLRLRLRLRLRLRL... and so on. 
For example, here is a situation that takes 6 steps to reach ZZZ:

LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)

Starting at AAA, follow the left/right instructions. How many steps are required to reach ZZZ?
"""

import re
import math as m

directions, _, *graph = open('node_input.txt').read().split('\n')

graph = {n: d for n, *d in [re.findall('\w+', s) for s in graph]}
start = [n for n in graph if n.endswith('A')]

def solve(pos, i = 0):
    while not pos.endswith('Z'):
        dir = directions[i % len(directions)]
        pos = graph[pos][dir == 'R']
        i += 1
    return i

print(solve('AAA'), m.lcm(*map(solve,start)))