import pandas as pd
import numpy as np
import math

'''
https://adventofcode.com/2020/day/6

'''

# Part 1

file_loc = r'aoc_6_input.txt'
response_list = []

with open(file_loc, 'r') as fp:
    for line in fp:
        response_list.append(line.split('\n')[0])

print(response_list)


def get_ans_count_1(res_list):
    answer_list = []
    answer_count = []
    for response in res_list:
        if response == '':
            unique_list = list(set(answer_list))
            ans_count = len(unique_list)
            answer_count.append(ans_count)
            answer_list = []
        else:
            for chars in response:
                answer_list.append(chars)
    return sum(answer_count)


def get_ans_count_2(res_list):
    answer_list = []
    answer_count = []
    count = 0
    for response in res_list:
        if response == '':
            if count != 1:
                ans_series = pd.Series(answer_list)
                cond = ans_series.value_counts() == count
                unique_list = list(ans_series.value_counts()[cond].index)
                ans_count = len(unique_list)
                answer_count.append(ans_count)
                answer_list = []
                count = 0
            else:
                unique_list = answer_list
                ans_count = len(unique_list)
                answer_count.append(ans_count)
                answer_list = []
                count = 0
        else:
            for chars in response:
                answer_list.append(chars)
            count += 1
    return sum(answer_count)


test_list = ['abc', '', 'a', 'b', 'c', '', 'ab', 'ac', '', 'a', 'a', 'a', 'a', '', 'b', '']
print(get_ans_count_1(response_list))
print(get_ans_count_2(response_list))
