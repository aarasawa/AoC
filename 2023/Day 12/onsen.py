"""
There's just one problem - many of the springs have fallen into disrepair, so they're not actually sure 
which springs would even be safe to use! Worse yet, their condition records of which springs are damaged 
(your puzzle input) are also damaged! You'll need to help them repair the damaged records.

In the giant field just outside, the springs are arranged into rows. For each row, the condition records show 
every spring and whether it is operational (.) or damaged (#). This is the part of the condition records that is 
itself damaged; for some springs, it is simply unknown (?) whether the spring is operational or damaged.

However, the engineer that produced the condition records also duplicated some of this information in a different format! 
After the list of springs for a given row, the size of each contiguous group of damaged springs is listed in the order 
those groups appear in the row. This list always accounts for every damaged spring, and each number is the entire size 
of its contiguous group (that is, groups are always separated by at least one operational spring: #### would always be 4, 
 never 2,2).

So, condition records with no unknown spring conditions might look like this:

#.#.### 1,1,3
.#...#....###. 1,1,3
.#.###.#.###### 1,3,1,6
####.#...#... 4,1,1
#....######..#####. 1,6,5
.###.##....# 3,2,1
However, the condition records are partially damaged; some of the springs' conditions are actually unknown (?). For example:

???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
Equipped with this information, it is your job to figure out how many different arrangements of operational and 
broken springs fit the given criteria in each row.

In the first line (???.### 1,1,3), there is exactly one way separate groups of one, one, and three broken springs 
(in that order) can appear in that row: the first three unknown springs must be broken, then operational, then 
broken (#.#), making the whole row #.#.###.

The second line is more interesting: .??..??...?##. 1,1,3 could be a total of four different arrangements. 
The last ? must always be broken (to satisfy the final contiguous group of three broken springs), and each ?? 
must hide exactly one of the two broken springs. (Neither ?? could be both broken springs or they would form a 
single contiguous group of two; if that were true, the numbers afterward would have been 2,3 instead.) 
Since each ?? can either be #. or .#, there are four possible arrangements of springs.

The last line is actually consistent with ten different arrangements! Because the first number is 3, the first and 
second ? must both be . (if either were #, the first number would have to be 4 or higher). However, the remaining run of 
unknown spring conditions have many different ways they could hold groups of two and one broken springs:

?###???????? 3,2,1
.###.##.#...
.###.##..#..
.###.##...#.
.###.##....#
.###..##.#..
.###..##..#.
.###..##...#
.###...##.#.
.###...##..#
.###....##.#
In this example, the number of possible arrangements for each row is:

???.### 1,1,3 - 1 arrangement
.??..??...?##. 1,1,3 - 4 arrangements
?#?#?#?#?#?#?#? 1,3,1,6 - 1 arrangement
????.#...#... 4,1,1 - 1 arrangement
????.######..#####. 1,6,5 - 4 arrangements
?###???????? 3,2,1 - 10 arrangements
Adding all of the possible arrangement counts together produces a total of 21 arrangements.

For each row, count all of the different arrangements of operational and broken springs that meet the given criteria. 
What is the sum of those counts?

forgot to reference, was from subreddit for Day 12
"""

from functools import cache

@cache
def recurse(lava, springs, result=0):
    if not springs:
        return '#' not in lava
    current, springs = springs[0], springs[1:]
    for i in range(len(lava) - sum(springs) - len(springs) - current + 1):
        if "#" in lava[:i]:
            break
        if (nxt := i + current) <= len(lava) and '.' not in lava[i : nxt] and lava[nxt : nxt + 1] != "#":
            result += recurse(lava[nxt + 1:], springs)
    return result


with open("onsen_input.txt", "r") as file:
    data = [x.split() for x in file.read().splitlines()]
    p1, p2 = 0, 0
    for e, (lava, springs) in enumerate(data):
        p1 += recurse(lava, (springs := tuple(map(int, springs.split(",")))))
        p2 += recurse("?".join([lava] * 5), springs * 5)
    print(p1, p2)