import pandas as pd
import numpy as np

'''
https://adventofcode.com/2021/day/10

'''

# Part 1
file_loc = r'aoc_10_input.txt'
char_dict = {
    '{': {'lh': True, 'pair': '}'},
    '<': {'lh': True, 'pair': '>'},
    '[': {'lh': True, 'pair': ']'},
    '(': {'lh': True, 'pair': ')'}
}

score = {
    '}': 1197,
    ')': 3,
    ']': 57,
    '>': 25137,
}


inc_score = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}


def check_line(char_lst):
    check_flag = False
    illegal_char = ''

    for index, char in enumerate(char_lst):
        if char not in char_dict.keys():
            if char_dict[char_lst[index-1]]['pair'] != char:
                check_flag = True
                illegal_char = char
                break
            else:
                new_lst = char_lst.copy()
                del new_lst[index-1:index+1]
                return check_line(new_lst)

    return check_flag, illegal_char, char_lst


ans = []
inc_ans = []
sum = 0
with open(file_loc, 'r') as fp:
    for line in fp:
        line = list(line.strip())
        flag, illegal, char_lst = check_line(line)
        if flag:
            ans.append(illegal)
            sum += score[illegal]
        else:
            inc_sum = 0
            for char in char_lst[::-1]:
                inc_sum *= 5
                inc_sum += inc_score[char]
            inc_ans.append(inc_sum)

print(len(ans))
print(sum)
print(inc_ans.sort())
print(inc_ans[len(inc_ans)//2])

