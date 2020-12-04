import pandas as pd
import numpy as np

'''
https://adventofcode.com/2020/day/2

'''

# Part 1

file_loc = r'aoc_2_input.txt'
password_list = []
flag_list1 = []
flag_list2 = []


def pwd_check(min_c, max_c, char, pwd):
    char_count = pwd.count(char)
    flag = 0
    if (char_count >= min_c) & (char_count <= max_c):
        flag = 1
    return flag


def pwd_check_2(min_c, max_c, char, pwd):
    char_list = list(pwd)
    flag = 0
    if (char_list[min_c] == char) & (char_list[max_c] == char):
        flag = 0
    elif (char_list[min_c] == char) | (char_list[max_c] == char):
        flag = 1
    return flag


with open(file_loc, 'r') as fp:
    for line in fp:
        password_list.append(line.split('\n')[0])

for pwds in password_list:
    pwd_key = pwds.split(':')[0]
    pwd_value = pwds.split(':')[1]
    min_count = int(pwd_key.split('-')[0])
    max_count = int(pwd_key.split('-')[1].split(' ')[0])
    char_check = pwd_key.split('-')[1].split(' ')[1]
    flag_list1.append(pwd_check(min_count, max_count, char_check, pwd_value))
    flag_list2.append(pwd_check_2(min_count, max_count, char_check, pwd_value))

print('Part-1')
print("Number of valid passwords = {}".format(sum(flag_list1)))

print('Part-2')
print("Number of valid passwords = {}".format(sum(flag_list2)))
