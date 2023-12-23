"""
There's a map of nearby hiking trails (your puzzle input) that indicates paths (.), forest (#), 
and steep slopes (^, >, v, and <).

For example:

#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
You're currently on the single path tile in the top row; your goal is to reach the single path tile in the bottom row. 
Because of all the mist from the waterfall, the slopes are probably quite icy; if you step onto a slope tile, your next 
step must be downhill (in the direction the arrow is pointing). To make sure you have the most scenic hike possible, 
never step onto the same tile twice. What is the longest hike you can take?

In the example above, the longest hike you can take is marked with O, and your starting position is marked S:

#S#####################
#OOOOOOO#########...###
#######O#########.#.###
###OOOOO#OOO>.###.#.###
###O#####O#O#.###.#.###
###OOOOO#O#O#.....#...#
###v###O#O#O#########.#
###...#O#O#OOOOOOO#...#
#####.#O#O#######O#.###
#.....#O#O#OOOOOOO#...#
#.#####O#O#O#########v#
#.#...#OOO#OOO###OOOOO#
#.#.#v#######O###O###O#
#...#.>.#...>OOO#O###O#
#####v#.#.###v#O#O###O#
#.....#...#...#O#O#OOO#
#.#########.###O#O#O###
#...###...#...#OOO#O###
###.###.#.###v#####O###
#...#...#.#.>.>.#.>O###
#.###.###.#.###.#.#O###
#.....###...###...#OOO#
#####################O#
This hike contains 94 steps. (The other possible hikes you could have taken were 90, 86, 82, 82, and 74 steps long.)

Find the longest hike you can take through the hiking trails listed on your map. How many steps long is the longest hike?
"""

from collections import defaultdict
from dataclasses import dataclass
from queue import Queue, PriorityQueue

@dataclass(frozen=True)
class Pos:
    row: int
    col: int
    def __add__(self, other):
        return Pos(row=self.row + other.row, col=self.col + other.col)
    def __lt__(self, other):
        return True

grid = []
with open('input', 'r') as f:
    for line in f.readlines():
        grid.append(line.strip())
n, m = len(grid), len(grid[0])
start = Pos(0, grid[0].find('.'))
goal = Pos(n-1, grid[n-1].find('.'))

print('n:', n, 'm:', m)
print('start:', start, 'goal:', goal)

def get_nbrs1(pos):
    for delta in (Pos(1, 0), Pos(-1, 0), Pos(0, 1), Pos(0, -1)):
        nbr = pos + delta
        if 0 <= nbr.row < n and 0 <= nbr.col < m:
            if grid[nbr.row][nbr.col] != '#':
                if grid[pos.row][pos.col] == '>' and delta != Pos(0, 1):
                    continue
                if grid[pos.row][pos.col] == '<' and delta != Pos(0, -1):
                    continue
                if grid[pos.row][pos.col] == '^' and delta != Pos(-1, 0):
                    continue
                if grid[pos.row][pos.col] == 'v' and delta != Pos(1, 0):
                    continue
                yield nbr

def dijkstra(start, goal, nbr_func):
    q = PriorityQueue()
    dist = {start: 0}
    came_from = {start: None}
    q.put((dist[start], start))

    while not q.empty():
        f_dist, current = q.get()
        if current == goal:
            return dist[current]
        if f_dist > dist[current]:
            continue
        for nbr in nbr_func(current):
            if nbr == came_from[current]:
                continue
            g_dist = dist[current] - 1
            if nbr in dist and dist[nbr] <= g_dist:
                continue
            dist[nbr] = g_dist
            q.put((dist[nbr], nbr))
            came_from[nbr] = current

# part 1
print('Part 1:', -dijkstra(start, goal, get_nbrs1))

# part 2
def get_nbrs2(pos):
    for delta in (Pos(1, 0), Pos(-1, 0), Pos(0, 1), Pos(0, -1)):
        nbr = pos + delta
        if 0 <= nbr.row < n and 0 <= nbr.col < m:
            if grid[nbr.row][nbr.col] != '#':
                yield nbr

class Graph:
    def __init__(self):
        self.edges = defaultdict(set)
        self.dist = {}
    def add_edge(self, u, v, d):
        self.edges[u].add(v)
        self.edges[v].add(u)
        self.dist[(u, v)] = d
        self.dist[(v, u)] = d
    def get_nbrs(self, u):
        return list(self.edges[u])

graph = Graph()

checkpoints = {start, goal}
for i in range(n):
    for j in range(m):
        if grid[i][j] == '#':
            continue
        if len(list(get_nbrs2(Pos(i, j)))) >= 3:
            checkpoints.add(Pos(i, j))

for checkpoint in checkpoints:
    dist = {checkpoint: 0}
    q = Queue()
    q.put(checkpoint)
    while not q.empty():
        current = q.get()
        for nbr in get_nbrs2(current):
            if nbr in dist:
                continue
            if nbr in checkpoints:
                graph.add_edge(checkpoint, nbr, dist[current] + 1)
                continue
            dist[nbr] = dist[current] + 1
            q.put(nbr)

def get_longest_path(start, goal, visited):
    if start == goal:
        return 0
    longest = None
    for nbr in graph.get_nbrs(start):
        if nbr in visited:
            continue
        b = get_longest_path(nbr, goal, visited | {start})
        if b is None:
            continue
        d = graph.dist[(start, nbr)]
        if longest is None:
            longest = b + d
        else:
            longest = max(longest, b + d)
    result = longest
    return result

print('Part 2:', get_longest_path(start, goal, set()))