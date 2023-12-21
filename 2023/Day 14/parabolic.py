"""
In short: if you move the rocks, you can focus the dish. The platform even has a control panel on the side 
that lets you tilt it in one of four directions! The rounded rocks (O) will roll when the platform is tilted, 
while the cube-shaped rocks (#) will stay in place. You note the positions of all of the empty spaces (.) and 
rocks (your puzzle input). For example:

O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
Start by tilting the lever so all of the rocks will slide north as far as they will go:

OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#....
You notice that the support beams along the north side of the platform are damaged; to ensure the platform 
doesn't collapse, you should calculate the total load on the north support beams.

The amount of load caused by a single rounded rock (O) is equal to the number of rows from the rock to the 
south edge of the platform, including the row the rock is on. (Cube-shaped rocks (#) don't contribute to load.) 
So, the amount of load caused by each rock in each row is as follows:

OOOO.#.O.. 10
OO..#....#  9
OO..O##..O  8
O..#.OO...  7
........#.  6
..#....#.#  5
..O..#.O.O  4
..O.......  3
#....###..  2
#....#....  1
The total load is the sum of the load caused by all of the rounded rocks. In this example, the total load is 136.

Tilt the platform so that the rounded rocks all roll north. Afterward, what is the total load on the north support beams?

reference: https://www.reddit.com/r/adventofcode/comments/18i0xtn/comment/kdae7uv/
"""
import itertools

with open('parabolic_input.txt') as f:
    txt = f.read()

grid = txt.replace('\n', '')

lines = txt.split('\n')
width = len(lines[0])
height = len(lines)

def reorder(sub, direction):
    return ''.join(reversed(sorted(sub)) if direction in 'nw' else sorted(sub))

def one_direction(grid, direction):
    if direction in 'ns':
        columns = [grid[i::height] for i in range(width)]
        for e,c in enumerate(columns):
            columns[e] = '#'.join(reorder(subc, direction) for subc in c.split('#'))
        return ''.join(itertools.chain(*zip(*columns)))
    else:   # we
        rows = [grid[i*width:(i+1)*width] for i in range(height)]
        for e,r in enumerate(rows):
            rows[e] = '#'.join(reorder(subr, direction) for subr in r.split('#'))
        return ''.join(rows)

def load(grid):
    columns = [grid[i::height] for i in range(width)]
    return sum(sum(i for i,c in zip(range(len(col), 0, -1), col) if c == 'O') for col in columns)

# part 1
print(load(one_direction(grid, 'n')))

# part 2

cycle = 0
goal = 1_000_000_000

cycle_cache = {}
found_cycle = False

while cycle < goal:
    for d in 'nwse':
        grid = one_direction(grid, d)

    cycle += 1

    if not found_cycle and (found_cycle := grid in cycle_cache):
        cycle_length = cycle - cycle_cache[grid]
        cycle += cycle_length * ((goal - cycle) // cycle_length)
    else:
        cycle_cache[grid] = cycle

print(load(grid))