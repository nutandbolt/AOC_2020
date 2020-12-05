import pandas as pd
import numpy as np
import math

'''
https://adventofcode.com/2020/day/4

'''

# Part 1

file_loc = r'aoc_4_input.txt'
passport_list = []

with open(file_loc, 'r') as fp:
    for line in fp:
        passport_list.append(line.split('\n')[0])

print(passport_list)
