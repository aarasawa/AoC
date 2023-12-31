"""
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters:
one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line.

For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 43, 14, and 76. Adding these together produces 281.

What is the sum of all the calibration values?
"""

import re

#clean and organize data
data = open('trebuchet_input.txt').read().strip()

#create an integer representation for numeric words in the strings
data = (
    data.replace('one', 'one1one')
    .replace('two', 'two2two')
    .replace('three', 'three3three')
    .replace('four', 'four4four')
    .replace('five', 'five5five')
    .replace('six', 'six6six')
    .replace('seven', 'seven7seven')
    .replace('eight', 'eight8eight')
    .replace('nine', 'nine9nine'))

#regex for finding digits using list comprehension
dg = data.split("\n")
dg = [re.findall("\d", x) for x in dg]

#sum of first and last digits for strings
final_txt = "The sum of all the calibration values is {}"
print(final_txt.format(sum(int(x[0] + x[-1]) for x in dg)))