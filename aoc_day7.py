import pandas as pd
import numpy as np
import math

'''
https://adventofcode.com/2020/day/7

'''

# Part 1

file_loc = r'aoc_7_input.txt'
bag_lists = []

with open(file_loc, 'r') as fp:
    for line in fp:
        bag_lists.append(line.split('\n')[0])
#print(bag_lists)


def bag_finder(bag_name, bag_name_lists):
    big_bag = []
    for bag_name_list in bag_name_lists:
        outer_bag = bag_name_list.split('contain')[0]
        inner_bags = bag_name_list.split('contain')[1]
        if bag_name in inner_bags:
            big_bag.append(outer_bag)
    return len(big_bag), big_bag


bags = ['shiny gold']
total_count = []
list_big_bags = []

for bag in bags:
    bag_count, big_bags = bag_finder(bags, bag_lists)
    total_count.append(bag_count)
    list_big_bags.append(big_bags)
print(bag_count)
print(big_bag)

