"""
While you wait, one of the Elves that works with the gardener heard how good you are at solving problems
and would like your help. He needs to get his steps in for the day, and so he'd like to know which garden
plots he can reach with exactly his remaining 64 steps.

He gives you an up-to-date map (your puzzle input) of his starting position (S), garden plots (.), and rocks (#). 
For example:

...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
The Elf starts at the starting position (S) which also counts as a garden plot. 
Then, he can take one step north, south, east, or west, but only onto tiles that are garden plots. 
This would allow him to reach any of the tiles marked O:

...........
.....###.#.
.###.##..#.
..#.#...#..
....#O#....
.##.OS####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
Then, he takes a second step. Since at this point he could be at either tile marked O, his second step would 
allow him to reach any garden plot that is one step north, south, east, or west of any tile that he could have 
reached after the first step:

...........
.....###.#.
.###.##..#.
..#.#O..#..
....#.#....
.##O.O####.
.##.O#...#.
.......##..
.##.#.####.
.##..##.##.
...........
After two steps, he could be at any of the tiles marked O above, including the starting position 
(either by going north-then-south or by going west-then-east).

A single third step leads to even more possibilities:

...........
.....###.#.
.###.##..#.
..#.#.O.#..
...O#O#....
.##.OS####.
.##O.#...#.
....O..##..
.##.#.####.
.##..##.##.
...........
He will continue like this until his steps for the day have been exhausted. After a total of 6 steps, he could reach 
any of the garden plots marked O:

...........
.....###.#.
.###.##.O#.
.O#O#O.O#..
O.O.#.#.O..
.##O.O####.
.##.O#O..#.
.O.O.O.##..
.##.#.####.
.##O.##.##.
...........
In this example, if the Elf's goal was to get exactly 6 more steps today, he could use them to reach any of 16 garden plots.

However, the Elf actually needs to get 64 steps today, and the map he's handed you is much larger than the example map.

Starting from the garden plot marked S on your map, how many garden plots could the Elf reach in exactly 64 steps?

reference: https://www.reddit.com/r/adventofcode/comments/18nevo3/
"""

G = {i + j * 1j: c for i, r in enumerate(open('input'))
                    for j, c in enumerate(r) if c in '.S'}

done = []
todo = {x for x in G if G[x] == 'S'}
cmod = lambda x: complex(x.real%131, x.imag%131)

#for range in 3 by 131 grid 
for s in range(3 * 131):
    if s == 64: print(len(todo))
    
    if s%131 == 65: done.append(len(todo))

    todo = {p + d for d in {1, -1, 1j, -1j}
                    for p in todo if cmod(p + d) in G}

f = lambda n, a, b, c: a + n * (b - a + (n - 1) * (c - b - b + a) // 2)
print(f(26501365 // 131, done))