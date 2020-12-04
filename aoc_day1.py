import pandas as pd
import numpy as np

'''
https://adventofcode.com/2020/day/1

'''

# Part 1

file_loc = r'aoc_1_input.txt'
expense_list = []

with open(file_loc,'r') as fp:
    for line in fp:
        expense_list.append(int(line))

flag = 0

for exp in expense_list:
    list_b = list(set(expense_list) - set([exp]))
    if flag == 1:
        break
    for exp_b in list_b:
        if exp + exp_b == 2020:
            flag = 1
            print('Part-1')
            print(' {} + {} = {} '.format(exp, exp_b, exp + exp_b))
            print(' {} * {} = {} '.format(exp, exp_b, exp * exp_b))
            break


# Part 2
flag = 0
for exp in expense_list:
    list_b = list(set(expense_list) - set([exp]))
    if flag == 1:
        break
    for exp_b in list_b:
        list_c = list(set(list_b) - set([exp_b]))
        if flag == 1:
            break
        for exp_c in list_c:
            if exp + exp_b + exp_c == 2020:
                flag = 1
                print('Part-2')
                print(' {} + {} + {}= {} '.format(exp, exp_b,exp_c, exp + exp_b + exp_c))
                print(' {} * {} * {}= {} '.format(exp, exp_b, exp_c,exp * exp_b * exp_c))
                break



