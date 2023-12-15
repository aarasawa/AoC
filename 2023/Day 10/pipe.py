"""
The pipes are arranged in a two-dimensional grid of tiles:

| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
Based on the acoustics of the animal's scurrying, you're confident the pipe that contains the animal 
is one large, continuous loop.

For example, here is a square loop of pipe:

.....
.F-7.
.|.|.
.L-J.
.....
If the animal had entered this loop in the northwest corner, the sketch would instead look like this:

.....
.S-7.
.|.|.
.L-J.
.....
In the above diagram, the S tile is still a 90-degree F bend: you can tell because of how the adjacent pipes connect to it.

Unfortunately, there are also many pipes that aren't connected to the loop! This sketch shows the same loop as above:

-L|F7
7S-7|
L|7||
-L-J|
L|-JF
In the above diagram, you can still figure out which pipes form the main loop: they're the ones connected to S, 
pipes those pipes connect to, pipes those pipes connect to, and so on. 
Every pipe in the main loop connects to its two neighbors (including S, which will have exactly two pipes connecting to it, 
and which is assumed to connect back to those two pipes).

Here is a sketch that contains a slightly more complex main loop:

..F7.
.FJ|.
SJ.L7
|F--J
LJ...
Here's the same example sketch with the extra, non-main-loop pipe tiles also shown:

7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
If you want to get out ahead of the animal, you should find the tile in the loop that is farthest from the starting position. 
Because the animal is in the pipe, it doesn't make sense to measure this by direct distance. 
Instead, you need to find the tile that would take the longest number of steps along the loop to reach from the starting point 
- regardless of which way around the loop the animal went.

In the first example with the square loop:

.....
.S-7.
.|.|.
.L-J.
.....
You can count the distance each tile in the loop is from the starting point like this:

.....
.012.
.1.3.
.234.
.....
In this example, the farthest point from the start is 4 steps away.

Here's the more complex loop again:

..F7.
.FJ|.
SJ.L7
|F--J
LJ...
Here are the distances for each tile on that loop:

..45.
.236.
01.78
14567
23...
Find the single giant loop starting at S. 
How many steps along the loop does it take to get from the starting position to the point farthest from the starting position?

reference: https://www.reddit.com/r/adventofcode/comments/18evyu9/comment/kcrhxwc
"""

""" maze = {complex(i,j): c for i,r in enumerate(open('pipe_input.txt'))
                        for j,c in enumerate(r.strip())}

N, S, E, W = -1, +1, +1j, -1j
dirs = {'|': (N, S), '-': (E, W), 'L': (N, E),
        'J': (N, W), '7': (S, W), 'F': (S, E),
        'S': (N, E, S, W), '.':()}

graph = {p: {p+d for d in dirs[c]} for p,c in maze.items()}
start = [p for p,d in graph.items() if len(d) == 4][0]

seen = {start}
while todo := graph[start]:
    node = todo.pop()
    seen |= {node}
    todo |= graph[node]-seen

irange = lambda n: [complex(n.real, i) for i in range(int(n.imag))]

print(len(seen)//2,
      sum(sum(maze[m] in "|JLS" and m in seen for m in irange(p)) % 2
          for p in set(maze)-seen)) """

S="data"
P="pipe_input.txt"
with open(P,"r") as f:
	R=f.read()
G=R.split("\n")
H=len(G)
W=len(G[0])

O = [[0]*W for _ in range(H)] # part 2

ax = -1
ay = -1
for i in range(H):
	for j in range(W):
		if "S" in G[i]:
			ax=i
			ay=G[i].find("S")
print(ax,ay)

# rightward downward leftward upward
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
happy = ["-7J", "|LJ", "-FL", "|F7"]
Sdirs = []
for i in range(4):
	pos = dirs[i]
	bx = ax+pos[0]
	by = ay+pos[1]
	if bx>=0 and bx<=H and by>=0 and by<=W and G[bx][by] in happy[i]:
		Sdirs.append(i)
print(Sdirs)
Svalid = 3 in Sdirs # part 2

# rightward downward leftward upward
transform = {
	(0,"-"): 0,
	(0,"7"): 1,
	(0,"J"): 3,
	(2,"-"): 2,
	(2,"F"): 1,
	(2,"L"): 3,
	(1,"|"): 1,
	(1,"L"): 0,
	(1,"J"): 2,
	(3,"|"): 3,
	(3,"F"): 0,
	(3,"7"): 2,
}

curdir = Sdirs[0]
cx = ax + dirs[curdir][0]
cy = ay + dirs[curdir][1]
ln = 1
O[ax][ay] = 1 # Part 2
while (cx,cy)!=(ax,ay):
	O[cx][cy] = 1 # Part 2
	ln += 1
	curdir = transform[(curdir,G[cx][cy])]
	cx = cx + dirs[curdir][0]
	cy = cy + dirs[curdir][1]
print(ln)
print(ln//2)

# End Part 1
# Begin Part 2

ct = 0
for i in range(H):
	inn = False
	for j in range(W):
		if O[i][j]:
			if G[i][j] in "|JL" or (G[i][j]=="S" and Svalid): inn = not inn
		else:
			ct += inn
print(ct)
