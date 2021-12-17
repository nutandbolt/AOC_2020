import pandas as pd
import numpy as np

'''
https://adventofcode.com/2021/day/9

'''

# Part 1
file_loc = r'aoc_9_input.txt'


def find_depth(input_df, check_lst, depth_lst):
    new_chk_lst = []
    rows, cols = input_df.shape
    if len(check_lst) == 0:
        depth_lst
        return len(depth_lst)
    for i, j in check_lst:
        if i != rows-1:
            if (int(input_df.iloc[i+1, j]) != 9) & ((i+1, j) not in check_lst) & ((i+1, j) not in depth_lst):
                new_chk_lst.append((i+1, j))
                depth_lst.append((i+1, j))
        if i !=0:
            if (int(input_df.iloc[i-1, j]) != 9) & ((i-1, j) not in check_lst) & ((i-1, j) not in depth_lst):
                new_chk_lst.append((i-1, j))
                depth_lst.append((i-1, j))
        if j !=0:
            if (int(input_df.iloc[i, j-1]) != 9) & ((i, j-1) not in check_lst) & ((i, j-1) not in depth_lst):
                new_chk_lst.append((i, j-1))
                depth_lst.append((i, j-1))
        if j != cols-1:
            if (int(input_df.iloc[i, j+1]) != 9) & ((i, j+1) not in check_lst) & ((i, j+1) not in depth_lst):
                new_chk_lst.append((i, j+1))
                depth_lst.append((i, j + 1))
    return find_depth(input_df, new_chk_lst, depth_lst)


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
low_points = []
for i in range(0, rows):
    for j in range(0, cols):
        value = int(height_map.iloc[i, j])
        if (check_bottom(height_map, i, j) & check_top(height_map, i, j) & check_right(height_map, i, j) &
                check_left(height_map, i, j)):
            risk_value = value + 1
            total += risk_value
            low_points.append((i, j))
            # print(f'{k}) ({i+1}, {j+1}), value= {value}\n')
            k += 1
print(total)
print(low_points)
# test = pd.DataFrame({
#                         0: [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
#                         1: [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
#                         2: [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
#                         3: [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
#                         4: [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]})
# test = test.T
check_points = [low_points[0]]
next_check = []
basin_size = []
index = 0
for m, n in low_points:
    print(index)
    basin_size.append(find_depth(height_map, [(m, n)], []))
    index += 1
basin_size.sort(reverse=True)
print(basin_size[0]*basin_size[1]*basin_size[2])





