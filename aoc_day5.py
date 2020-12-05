import pandas as pd
import numpy as np
import math

'''
https://adventofcode.com/2020/day/5

'''

# Part 1

file_loc = r'aoc_5_input.txt'
seat_list = []

with open(file_loc, 'r') as fp:
    for line in fp:
        seat_list.append(line.split('\n')[0])

print(seat_list)


def get_seat_id(seat_list):
    seat_id = []
    for seat in seat_list:
        seat_code_1 = list(seat)[0:7]
        seat_code_2 = list(seat)[7::]
        start_index = 0
        end_index = 128
        for code in seat_code_1:
            if code == 'F':
                end_index = (start_index + end_index)/2
            elif code == 'B':
                start_index = (start_index + end_index)/2
        if code == 'F':
            row = start_index
        else:
            row = end_index - 1

        start_index = 0
        end_index = 8
        for code in seat_code_2:
            if code == 'L':
                end_index = (start_index + end_index)/2
            elif code == 'R':
                start_index = (start_index + end_index)/2
        if code == 'L':
            col = start_index
        else:
            col = end_index - 1
        seat_id.append(row*8 + col)

    return seat_id


seat_id_list = sorted(get_seat_id(seat_list))
print("Part-1 \n")
print("Maximum Seat ID number found = {} ".format(int(max(seat_id_list))))

seat_id_diff = np.diff(seat_id_list)
index1 = np.where(seat_id_diff == 2)[0][0]
index2 = index1 + 1

seat_id = (index1 + index2)/2

print("\nPart-2\n ")
print("Seat ID = {}".format(seat_id))



