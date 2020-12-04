import pandas as pd
import numpy as np
import math

'''
https://adventofcode.com/2020/day/3

'''

# Part 1

file_loc = r'aoc_3_input.txt'
tree_list = []

with open(file_loc, 'r') as fp:
    for line in fp:
        tree_list.append(line.split('\n')[0])

shape = [len(tree_list), len(list(tree_list[0]))]
tree_array = np.zeros(shape)

for i, trees in enumerate(tree_list):
    for j, tree in enumerate(list(trees)):
        if tree == '#':
            tree_array[i][j] = 1


def find_tree_count(row_i, col_i, t_array):
    row_inc = row_i
    col_inc = col_i
    tree_array_ori = t_array.copy()

    i = 0
    j = 0

    tree_count = []
    while i < shape[0]:
        if t_array[i][j] == 1:
            tree_count.append(1)
        else :
            tree_count.append(0)
        i += row_inc
        j += col_inc

        if j > t_array.shape[1]-1:
            t_array = np.concatenate([t_array, tree_array_ori], axis=1)

    return sum(tree_count)


list_of_sol = []
print("Part-1 \n number of trees encountered = {}".format(find_tree_count(1, 3, tree_array)))

list_of_sol.append(find_tree_count(1, 1, tree_array))
list_of_sol.append(find_tree_count(1, 3, tree_array))
list_of_sol.append(find_tree_count(1, 5, tree_array))
list_of_sol.append(find_tree_count(1, 7, tree_array))
list_of_sol.append(find_tree_count(2, 1, tree_array))

print(list_of_sol)

print ("Part-2 \n Ans = {}".format(math.prod(list_of_sol)))


