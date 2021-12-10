import pandas as pd
import numpy as np

'''
https://adventofcode.com/2021/day/8

'''

# Part 1
file_loc = r'aoc_8_input.txt'


def decode(coded_text):

    number_dict = {'0': '', '1': coded_text[coded_text.str.len() == 2].values[0], '2': '',
                   '3': '',
                   '4': coded_text[coded_text.str.len() == 4].values[0], '5': '', '6': '',
                   '7': coded_text[coded_text.str.len() == 3].values[0],
                   '8': coded_text[coded_text.str.len() == 7].values[0], '9': ''}

    grid_dict = {'1': '', '2': '', '3': '', '4': '', '5': '', '6': '', '7': ''}

    temp_1 = coded_text[coded_text.str.len() == 2].values[0]
    temp_7 = coded_text[coded_text.str.len() == 3].values[0]
    temp_4 = coded_text[coded_text.str.len() == 4].values[0]
    temp_8 = coded_text[coded_text.str.len() == 7].values[0]

    grid_dict['2'] = list(set(temp_7) - set(temp_1))[0]

    temp_a, temp_b, temp_c = coded_text[coded_text.str.len() == 5].values
    for temp in [temp_a, temp_b, temp_c]:
        if set(temp).intersection(set(temp_1)) == set(temp_1):
            temp_3 = temp
            number_dict['3'] = temp

    grid_dict['4'] = list((set(temp_4) - set(temp_1)).intersection(set(temp_3)))[0]
    grid_dict['6'] = list(set(temp_3) - set(temp_1) - set(grid_dict['4']) - set(grid_dict['2']))[0]
    grid_dict['1'] = list(set(temp_4) - set(temp_1) - set(grid_dict['4']))[0]

    for temp in [temp_a, temp_b, temp_c]:
        if grid_dict['1'] in temp:
            temp_5 = temp
            number_dict['5'] = temp

    for temp in [temp_a, temp_b, temp_c]:
        if (temp != temp_5) & (temp != temp_3):
            temp_2 = temp
            number_dict['2'] = temp

    grid_dict['7'] = list(set(temp_5) - set(grid_dict['6']) - set(grid_dict['4']) -
                          set(grid_dict['2']) - set(grid_dict['1']))[0]

    grid_dict['3'] = list(set(temp_1) - set(grid_dict['7']))[0]

    grid_dict['5'] = list(set('abcdefg') - set(temp_5).union(set(grid_dict['3'])))[0]

    number_dict['6'] = grid_dict['2'] + grid_dict['1'] + grid_dict['4'] + grid_dict['7'] + grid_dict['6'] + grid_dict[
        '5']
    temp_6 = number_dict['6']
    number_dict['9'] = grid_dict['1'] + grid_dict['2'] + grid_dict['3'] + grid_dict['4'] + grid_dict['6'] + grid_dict[
        '7']
    temp_9 = number_dict['9']
    number_dict['0'] = grid_dict['1'] + grid_dict['2'] + grid_dict['3'] + grid_dict['5'] + grid_dict['6'] + grid_dict[
        '7']
    temp_0 = number_dict['0']

    return number_dict


with open(file_loc, 'r') as fp:
    total = 0
    for line in fp:
        code = pd.Series(line.split('|')[0].strip().split(' '))
        grid = decode(code)
        result = line.split('|')[1].strip().split(' ')
        display = ''

        for number in result:
            for key in grid.keys():
                if (len(set(grid[key]).intersection(set(number))) == len(set(grid[key]))) & \
                        (len(set(grid[key]).intersection(set(number))) == len(set(number))):
                    display += key
                    break

        total += int(display)

print(total)
