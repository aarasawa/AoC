"""
The contraption is aligned so that most of the beam bounces around the grid, but each tile on the grid converts some of the beam's light into heat to melt the rock in the cavern.

You note the layout of the contraption (your puzzle input). For example:

.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
The beam enters in the top-left corner from the left and heading to the right. Then, its behavior depends on what 
it encounters as it moves:

If the beam encounters empty space (.), it continues in the same direction.
If the beam encounters a mirror (/ or \), the beam is reflected 90 degrees depending on the angle of the mirror. 
For instance, a rightward-moving beam that encounters a / mirror would continue upward in the mirror's column, 
while a rightward-moving beam that encounters a \ mirror would continue downward from the mirror's column.
If the beam encounters the pointy end of a splitter (| or -), the beam passes through the splitter as if the 
splitter were empty space. For instance, a rightward-moving beam that encounters a - splitter would continue in 
the same direction.
If the beam encounters the flat side of a splitter (| or -), the beam is split into two beams going in each of the 
two directions the splitter's pointy ends are pointing. For instance, a rightward-moving beam that encounters a | splitter 
would split into two beams: one that continues upward from the splitter's column and one that continues downward from the 
splitter's column.
Beams do not interact with other beams; a tile can have many beams passing through it at the same time. 
A tile is energized if that tile has at least one beam pass through it, reflect in it, or split in it.

In the above example, here is how the beam of light bounces around the contraption:

>|<<<\....
|v-.\^....
.v...|->>>
.v...v^.|.
.v...v^...
.v...v^..\
.v../2\\..
<->-/vv|..
.|<<<2-|.\
.v//.|.v..
Beams are only shown on empty tiles; arrows indicate the direction of the beams. If a tile contains beams moving in 
multiple directions, the number of distinct directions is shown instead. Here is the same diagram but instead only 
showing whether a tile is energized (#) or not (.):

######....
.#...#....
.#...#####
.#...##...
.#...##...
.#...##...
.#..####..
########..
.#######..
.#...#.#..
Ultimately, in this example, 46 tiles become energized.

The light isn't energizing enough tiles to produce lava; to debug the contraption, you need to start by analyzing the 
current situation. With the beam starting in the top-left heading right, how many tiles end up being energized?

reference: https://www.reddit.com/r/adventofcode/comments/18jjpfk/comment/kdkz6lc/
"""

g = {complex(i,j): c for j, r in enumerate(open('beam_input.txt'))
                     for i, c in enumerate(r.strip())}

def fn(todo):
    done = set()
    while todo:
        pos, dir = todo.pop()
        while not (pos, dir) in done:
            done.add((pos, dir))
            pos += dir
            match g.get(pos):
                case '|': dir = 1j; todo.append((pos, -dir))
                case '-': dir = -1; todo.append((pos, -dir))
                case '/': dir = -complex(dir.imag, dir.real)
                case '\\': dir = complex(dir.imag, dir.real)
                case None: break

    return len(set(pos for pos, _ in done)) - 1

print(fn([(-1, 1)]))

print(max(map(fn, ([(pos-dir, dir)] for dir in (1,1j,-1,-1j)
                        for pos in g if pos-dir not in g))))