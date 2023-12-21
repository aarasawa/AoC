"""
You note down the patterns of ash (.) and rocks (#) that you see as you walk (your puzzle input); perhaps by 
carefully analyzing these patterns, you can figure out where the mirrors are!

For example:

#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
To find the reflection in each pattern, you need to find a perfect reflection across either a horizontal line 
between two rows or across a vertical line between two columns.

In the first pattern, the reflection is across a vertical line between two columns; arrows on each of the two 
columns point at the line between the columns:

123456789
    ><   
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.
    ><   
123456789
In this pattern, the line of reflection is the vertical line between columns 5 and 6. Because the vertical 
line is not perfectly in the middle of the pattern, part of the pattern (column 1) has nowhere to reflect onto 
and can be ignored; every other column has a reflected column within the pattern and must match exactly: column 
2 matches column 9, column 3 matches 8, 4 matches 7, and 5 matches 6.

The second pattern reflects across a horizontal line instead:

1 #...##..# 1
2 #....#..# 2
3 ..##..### 3
4v#####.##.v4
5^#####.##.^5
6 ..##..### 6
7 #....#..# 7
This pattern reflects across the horizontal line between rows 4 and 5. Row 1 would reflect with a hypothetical row 8, 
but since that's not in the pattern, row 1 doesn't need to match anything. The remaining rows match: row 2 matches row 7, 
row 3 matches row 6, and row 4 matches row 5.

To summarize your pattern notes, add up the number of columns to the left of each vertical line of reflection; to that, 
also add 100 multiplied by the number of rows above each horizontal line of reflection. In the above example, 
the first pattern's vertical line has 5 columns to its left and the second pattern's horizontal line has 4 rows above it,
a total of 405.

Find the line of reflection in each of the patterns in your notes. What number do you get after summarizing 
all of your notes?

reference: https://www.reddit.com/r/adventofcode/comments/18h940b/comment/kd5baa8/
"""

ps = list(map(str.split, open('lava_input.txt').read().split('\n\n')))

def f(p):
    for i in range(len(p)):
        if sum(c != d for l,m in zip(p[i-1::-1], p[i:])
                      for c,d in zip(l, m)) == s: return i
    else: return 0

for s in 0,1: print(sum(100 * f(p) + f([*zip(*p)]) for p in ps))