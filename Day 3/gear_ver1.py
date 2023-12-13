"""
The engine schematic (your puzzle input) consists of a visual representation of the engine. 
There are lots of numbers and symbols you don't really understand, but apparently any number 
adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. 
(Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 
114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part
 number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers 
in the engine schematic?
"""

import re
import math as m

gears = list(open('gear_input.txt'))

# get the locations for symbols in the schematics
syms = {(x, y): [] for x in range(140) for y in range(140) if gears[x][y] not in '0123456789.'}

# feed in schematic data by row and enumerate with row numbers
for r_num, row in enumerate(gears):

    # find numbers in the row using regex
    for digit in re.finditer(r'\d+', row):

        # create a dictionary of coordinates that surround the digits in the schematic
        digit_borders = {(i, j) for i in (r_num-1, r_num, r_num+1) for j in range(digit.start()-1, digit.end()+1)}

        # record symbols found around a schematic value into the symbol dictionary
        for coords in digit_borders & syms.keys():
            #print(digit_borders & syms.keys())
            syms[coords].append(int(digit.group()))

print(sum(sum(item) for item in syms.values()))
print(sum(m.prod(item) for item in syms.values() if len(item) == 2))