import pandas as pd
import numpy as np

'''
https://adventofcode.com/2021/day/2

'''

# Part 1

file_loc = r'aoc_2_input.txt'
depth_lst = []
horizontal_lst = []
hor_distance = 0
ver_distance = 0

with open(file_loc, 'r') as fp:
    for line in fp:
        direction = line.split(' ')[0]
        value = int(line.split(' ')[1])

        if direction == 'forward':
            hor_distance += value
        elif direction == 'up':
            ver_distance -= value
        elif direction == 'down':
            ver_distance += value
        else:
            print(direction)

ans = ver_distance * hor_distance

print(ans)

# part 2
hor_distance = 0
ver_distance = 0
aim = 0
with open(file_loc, 'r') as fp:
    for line in fp:
        direction = line.split(' ')[0]
        value = int(line.split(' ')[1])

        if direction == 'forward':
            hor_distance += value
            ver_distance += aim*value
        elif direction == 'up':
            aim -= value
        elif direction == 'down':
            aim += value
        else:
            print(direction)

ans = ver_distance * hor_distance

print(ans)
