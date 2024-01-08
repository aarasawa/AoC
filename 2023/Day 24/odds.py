"""
Due to strong, probably-magical winds, the hailstones are all flying through the air in perfectly linear trajectories. 
You make a note of each hailstone's position and velocity (your puzzle input). For example:

19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
Each line of text corresponds to the position and velocity of a single hailstone. The positions indicate where the 
hailstones are right now (at time 0). The velocities are constant and indicate exactly how far each hailstone will 
move in one nanosecond.

Each line of text uses the format px py pz @ vx vy vz. For instance, the hailstone specified by 20, 19, 15 @ 1, -5, -3 
has initial X position 20, Y position 19, Z position 15, X velocity 1, Y velocity -5, and Z velocity -3. 
After one nanosecond, the hailstone would be at 21, 14, 12.

Perhaps you won't have to do anything. How likely are the hailstones to collide with each other and smash into tiny ice 
crystals?

To estimate this, consider only the X and Y axes; ignore the Z axis. Looking forward in time, how many of the hailstones' 
paths will intersect within a test area? (The hailstones themselves don't have to collide, just test for intersections 
between the paths they will trace.)

In this example, look for intersections that happen with an X and Y position each at least 7 and at most 27; in your actual 
data, you'll need to check a much larger test area. Comparing all pairs of hailstones' future paths produces the following
results:

Hailstone A: 19, 13, 30 @ -2, 1, -2
Hailstone B: 18, 19, 22 @ -1, -1, -2
Hailstones' paths will cross inside the test area (at x=14.333, y=15.333).

Hailstone A: 19, 13, 30 @ -2, 1, -2
Hailstone B: 20, 25, 34 @ -2, -2, -4
Hailstones' paths will cross inside the test area (at x=11.667, y=16.667).

Hailstone A: 19, 13, 30 @ -2, 1, -2
Hailstone B: 12, 31, 28 @ -1, -2, -1
Hailstones' paths will cross outside the test area (at x=6.2, y=19.4).

Hailstone A: 19, 13, 30 @ -2, 1, -2
Hailstone B: 20, 19, 15 @ 1, -5, -3
Hailstones' paths crossed in the past for hailstone A.

Hailstone A: 18, 19, 22 @ -1, -1, -2
Hailstone B: 20, 25, 34 @ -2, -2, -4
Hailstones' paths are parallel; they never intersect.

Hailstone A: 18, 19, 22 @ -1, -1, -2
Hailstone B: 12, 31, 28 @ -1, -2, -1
Hailstones' paths will cross outside the test area (at x=-6, y=-5).

Hailstone A: 18, 19, 22 @ -1, -1, -2
Hailstone B: 20, 19, 15 @ 1, -5, -3
Hailstones' paths crossed in the past for both hailstones.

Hailstone A: 20, 25, 34 @ -2, -2, -4
Hailstone B: 12, 31, 28 @ -1, -2, -1
Hailstones' paths will cross outside the test area (at x=-2, y=3).

Hailstone A: 20, 25, 34 @ -2, -2, -4
Hailstone B: 20, 19, 15 @ 1, -5, -3
Hailstones' paths crossed in the past for hailstone B.

Hailstone A: 12, 31, 28 @ -1, -2, -1
Hailstone B: 20, 19, 15 @ 1, -5, -3
Hailstones' paths crossed in the past for both hailstones.
So, in this example, 2 hailstones' future paths cross inside the boundaries of the test area.

However, you'll need to search a much larger test area if you want to see if any hailstones might collide. 
Look for intersections that happen with an X and Y position each at least 200000000000000 and at most 400000000000000. 
Disregard the Z axis entirely.

Considering only the X and Y axes, check all pairs of hailstones' future paths for intersections. How many of these 
intersections occur within the test area?

reference: https://github.com/mebeim/aoc/blob/master/2023/solutions/day24.py
"""

import sys
from collections import defaultdict, deque

def neighbors(grid, r, c, ignore_slopes):
	cell = grid[r][c]

	if ignore_slopes or cell == '.':
		for r, c in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
			if grid[r][c] != '#':
				yield r, c
	elif cell == 'v': yield (r + 1, c)
	elif cell == '^': yield (r - 1, c)
	elif cell == '>': yield (r, c + 1)
	elif cell == '<': yield (r, c - 1)

def num_neighbors(grid, r, c, ignore_slopes):
	if ignore_slopes or grid[r][c] == '.':
		return sum(grid[r][c] != '#' for r, c in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)))
	return 1

def is_node(grid, rc, src, dst, ignore_slopes):
	return rc == src or rc == dst or num_neighbors(grid, *rc, ignore_slopes) > 2

def adjacent_nodes(grid, rc, src, dst, ignore_slopes):
	q = deque([(rc, 0)])
	seen = set()

	while q:
		rc, dist = q.popleft()
		seen.add(rc)

		for n in neighbors(grid, *rc, ignore_slopes):
			if n in seen:
				continue

			if is_node(grid, n, src, dst, ignore_slopes):
				yield (n, dist + 1)
				continue

			q.append((n, dist + 1))

def graph_from_grid(grid, src, dst, ignore_slopes=False):
	g = defaultdict(list)
	q = deque([src])
	seen = set()

	while q:
		rc = q.popleft()
		if rc in seen:
			continue

		seen.add(rc)

		for n, weight in adjacent_nodes(grid, rc, src, dst, ignore_slopes):
			g[rc].append((n, weight))
			q.append(n)

	return g

def longest_path(g, cur, dst, distance=0, seen=set()):
	if cur == dst:
		return distance

	best = 0
	seen.add(cur)

	for neighbor, weight in g[cur]:
		if neighbor in seen:
			continue

		best = max(best, longest_path(g, neighbor, dst, distance + weight))

	seen.remove(cur)
	return best


# Open the first argument as input or use stdin if no arguments were given
fin = open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin

grid = list(map(list, fin.read().splitlines()))
height, width = len(grid), len(grid[0])

grid[0][1] = '#'
grid[height - 1][width - 2] = '#'

src = (1, 1)
dst = (height - 2, width - 2)

g = graph_from_grid(grid, src, dst)
pathlen = longest_path(g, src, dst) + 2
print('Part 1:', pathlen)

g = graph_from_grid(grid, src, dst, ignore_slopes=True)
pathlen = longest_path(g, src, dst) + 2
print('Part 2:', pathlen)