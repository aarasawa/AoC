import re

file = open('trebuchet_input.txt')
sum = 0

for input_line in file:
    all_digits = re.findall(r"\d", input_line)
    concat_digits = all_digits[0] + all_digits[-1]
    sum = sum + int(concat_digits)

final_txt = "The sum of all the calibration values is {}"
print(final_txt.format(sum))