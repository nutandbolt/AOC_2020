import pandas as pd
import numpy as np

'''
https://adventofcode.com/2021/day/9

'''

# Part 1
file_loc = r'aoc_9_input.txt'


def check_right(height_map, i, j):
    right = False
    try:
        if int(height_map.iloc[i, j]) < int(height_map.iloc[i, j+1]):
            right = True
    except IndexError:
        right = True
    return right


def check_left(height_map, i, j):
    left = False
    if j == 0:
        # iloc wont give index error for negative index
        return True
    try:
        if int(height_map.iloc[i, j]) < int(height_map.iloc[i, j-1]):
            left = True
    except IndexError:
        left = True
    return left


def check_top(height_map, i, j):
    top = False
    if i == 0:
        # iloc wont give index error for negative index
        return True
    try:
        if int(height_map.iloc[i, j]) < int(height_map.iloc[i-1, j]):
            top = True
    except IndexError:
        top = True
    return top


def check_bottom(height_map, i, j):
    bottom = False
    try:
        if int(height_map.iloc[i, j]) < int(height_map.iloc[i+1, j]):
            bottom = True
    except IndexError:
        bottom = True
    return bottom


height_map = pd.DataFrame(columns=range(0, 5))
with open(file_loc, 'r') as fp:
    for line in fp:
        line = line.strip()
        temp_df = pd.DataFrame([list(line)])
        height_map = pd.concat([height_map, temp_df])

rows, cols = height_map.shape

total = 0
k = 1
for i in range(0, rows):
    for j in range(0, cols):
        value = int(height_map.iloc[i, j])
        if (check_bottom(height_map, i, j) & check_top(height_map, i, j) & check_right(height_map, i, j) &
                check_left(height_map, i, j)):
            risk_value = value + 1
            total += risk_value
            print(f'{k}) ({i+1}, {j+1}), value= {value}\n')
            k += 1
print(total)

