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

reference: https://www.reddit.com/r/adventofcode/comments/18pnycy/comment/keqf8uq/
"""

import itertools as it

InputList = []
with open("odds.txt", "r") as data:
    for t in data:
        P, V = t.strip().split(" @ ")
        PX, PY, PZ = list(map(int, P.split(", ")))
        VX, VY, VZ = list(map(int, V.split(", ")))
        NewTuple = (PX, PY, PZ, VX, VY, VZ)
        InputList.append(NewTuple)

#PX1 + VX1*t = PX2 + VX2*t
#PX1 - PX2 = VX2*t - VX1*t
#(PX1-PX2)/(VX2-VX1) = t

#y = mx + b
#m = avy/avx
#b = apy - m*apx
#m1x + b1 = m2x + b2
#m1x - m2x = b2 - b1
#x = (b2-b1)/(m1-m2)
#200000000000000
#400000000000000
        
NumHails = len(InputList)
Part1Answer = 0
NumCombos = 0
Min = 200000000000000
Max = 400000000000000
InputList.sort()
for A, B in it.combinations(InputList, 2):
    NumCombos += 1
    APX, APY, APZ, AVX, AVY, AVZ = A
    BPX, BPY, BPZ, BVX, BVY, BVZ = B
    MA = (AVY/AVX)
    MB = (BVY/BVX)
    CA = APY - (MA*APX)
    CB = BPY - (MB*BPX)
    if MA == MB:
        continue
    XPos = (CB-CA)/(MA-MB)
    YPos = MA*XPos + CA
    if (XPos < APX and AVX > 0) or (XPos > APX and AVX < 0) or (XPos < BPX and BVX > 0) or (XPos > BPX and BVX < 0):
        continue
    if Min <= XPos <= Max and Min <= YPos <= Max:
        Part1Answer += 1




PotentialXSet = None
PotentialYSet = None
PotentialZSet = None
for A, B in it.combinations(InputList, 2):
    APX, APY, APZ, AVX, AVY, AVZ = A
    BPX, BPY, BPZ, BVX, BVY, BVZ = B

    if AVX == BVX and abs(AVX) > 100:
        NewXSet = set()
        Difference = BPX - APX
        for v in range(-1000, 1000):
            if v == AVX:
                continue
            if Difference % (v-AVX) == 0:
                NewXSet.add(v)
        if PotentialXSet != None:
            PotentialXSet = PotentialXSet & NewXSet
        else:
            PotentialXSet = NewXSet.copy()
    if AVY == BVY and abs(AVY) > 100:
        NewYSet = set()
        Difference = BPY - APY
        for v in range(-1000, 1000):
            if v == AVY:
                continue
            if Difference % (v-AVY) == 0:
                NewYSet.add(v)
        if PotentialYSet != None:
            PotentialYSet = PotentialYSet & NewYSet
        else:
            PotentialYSet = NewYSet.copy()
    if AVZ == BVZ and abs(AVZ) > 100:
        NewZSet = set()
        Difference = BPZ - APZ
        for v in range(-1000, 1000):
            if v == AVZ:
                continue
            if Difference % (v-AVZ) == 0:
                NewZSet.add(v)
        if PotentialZSet != None:
            PotentialZSet = PotentialZSet & NewZSet
        else:
            PotentialZSet = NewZSet.copy()

print(PotentialXSet, PotentialYSet, PotentialZSet)
RVX, RVY, RVZ = PotentialXSet.pop(), PotentialYSet.pop(), PotentialZSet.pop()

APX, APY, APZ, AVX, AVY, AVZ = InputList[0]
BPX, BPY, BPZ, BVX, BVY, BVZ = InputList[1]
MA = (AVY-RVY)/(AVX-RVX)
MB = (BVY-RVY)/(BVX-RVX)
CA = APY - (MA*APX)
CB = BPY - (MB*BPX)
XPos = int((CB-CA)/(MA-MB))
YPos = int(MA*XPos + CA)
Time = (XPos - APX)//(AVX-RVX)
ZPos = APZ + (AVZ - RVZ)*Time

print(XPos, YPos, ZPos)
Part2Answer = XPos + YPos + ZPos


print(f"{Part1Answer = }")
print(f"{Part2Answer = }")