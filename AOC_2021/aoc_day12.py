import pandas as pd
import numpy as np

'''
https://adventofcode.com/2021/day/12

'''

# Part 1
def dfs(node_dict, node):
    traverse_lst = node_dict[node]
    path_lst = []
    for t_node in traverse_lst:
        path_lst.append(t_node)
        t_node_lst = node_dict[t_node]
        for m_node in t_node_lst:
            path_lst.append(m_node)
            if m_node == 'end':
                return path_lst
            else:
                return dfs(node_dict, m_node)


file_loc = r'aoc_12_input.txt'
node_dict = {}
with open(file_loc, 'r') as fp:
    for line in fp:
        nodei, nodej = line.strip().split('-')
        if nodei not in node_dict.keys():
            node_dict[nodei] = []
        node_dict[nodei].append(nodej)
print(node_dict)
node = 'start'
paths = dfs(node_dict, node)
