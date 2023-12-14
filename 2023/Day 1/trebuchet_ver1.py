"""

The newly-improved calibration document consists of lines of text; each line originally contained a specific 
calibration value that the Elves now need to recover. On each line, the calibration value can be found by 
combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. 
Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
"""

import re

#clean and organize data
data = open('trebuchet_input.txt').read().strip().split("\n")

#regex for finding digits using list comprehension
dg = [re.findall("\d", x) for x in data]

#sum of first and last digits for strings
final_txt = "The sum of all the calibration values is {}"
print(final_txt.format(sum(int(x[0] + x[-1]) for x in dg)))