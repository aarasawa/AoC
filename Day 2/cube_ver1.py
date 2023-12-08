"""
You play several games and record the information from each game (your puzzle input). Each game 
is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated 
list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

For example, the record of a few games might look like this:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

In game 1, three sets of cubes are revealed from the bag (and then put back again). The first 
set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; 
the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag contained only 
12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that 
configuration. However, game 3 would have been impossible because at one point the Elf showed you 
20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 
15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.

Determine which games would have been possible if the bag had been loaded with only 
12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
"""
import re

red_cubes = 12
green_cubes = 13
blue_cubes = 14

game_id_total = 0
red_total = 0
green_total = 0
blue_total = 0

with open('cube_input.txt') as f:
    data = f.read().strip().split('\n')

def init_and_rezero_counters():
    global red_total
    red_total = 0
    global green_total
    green_total = 0
    global blue_total
    blue_total = 0

def color_total_adder(color, num):
    if color == 'red':
        global red_total
        red_total = red_total + num
    if color == 'green':
        global green_total 
        green_total = green_total + num
    if color == 'blue':
        global blue_total
        blue_total = blue_total + num

def total_comparison_and_game_id_sum(num):
    print(red_total, green_total, blue_total)
    if (red_total <= red_cubes) and (green_total <= green_cubes) and (blue_total <= blue_cubes):
        global game_id_total
        game_id_total = game_id_total + num

def main(input):
    init_and_rezero_counters()
    game_num = input[0]
    for chance in input[1:]:
        times_rolled, color_rolled = chance.strip().split(' ')
        color_total_adder(color_rolled, int(times_rolled))
        #print(red_total, green_total, blue_total)
    total_comparison_and_game_id_sum(int(game_num))
    print(game_id_total)

for x in data:
    fi = re.sub('Game ', '', x)
    si = re.split(': |, |;', fi)
    print(si)
    #everything is now split into 'num color' format
    #func is being fed by row
    main(si)