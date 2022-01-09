import pandas as pd
import numpy as np

'''
https://adventofcode.com/2021/day/6

'''

# Part 1

curr_state = np.array([3, 4, 3, 1, 2])
# curr_state = np.array([1, 1, 1, 3, 3, 2, 1, 1, 1, 1, 1, 4, 4, 1, 4, 1, 4, 1, 1, 4, 1, 1, 1, 3, 3, 2, 3, 1, 2, 1, 1, 1,
#               1, 1, 1,
#               1, 3, 4, 1, 1, 4, 3, 1, 2, 3, 1, 1, 1, 5, 2, 1, 1, 1, 1, 2, 1, 2, 5, 2, 2, 1, 1, 1, 3, 1, 1, 1, 4, 1, 1,
#               1, 1, 1, 3, 3, 2, 1, 1, 3, 1, 4, 1, 2, 1, 5, 1, 4, 2, 1, 1, 5, 1, 1, 1, 1, 4, 3, 1, 3, 2, 1, 4, 1, 1, 2,
#               1, 4, 4, 5, 1, 3, 1, 1, 1, 1, 2, 1, 4, 4, 1, 1, 1, 3, 1, 5, 1, 1, 1, 1, 1, 3, 2, 5, 1, 5, 4, 1, 4, 1, 3,
#               5, 1, 2, 5, 4, 3, 3, 2, 4, 1, 5, 1, 1, 2, 4, 1, 1, 1, 1, 2, 4, 1, 2, 5, 1, 4, 1, 4, 2, 5, 4, 1, 1, 2, 2,
#               4, 1, 5, 1, 4, 3, 3, 2, 3, 1, 2, 3, 1, 4, 1, 1, 1, 3, 5, 1, 1, 1, 3, 5, 1, 1, 4, 1, 4, 4, 1, 3, 1, 1, 1,
#               2, 3, 3, 2, 5, 1, 2, 1, 1, 2, 2, 1, 3, 4, 1, 3, 5, 1, 3, 4, 3, 5, 1, 1, 5, 1, 3, 3, 2, 1, 5, 1, 1, 3, 1,
#               1, 3, 1, 2, 1, 3, 2, 5, 1, 3, 1, 1, 3, 5, 1, 1, 1, 1, 2, 1, 2, 4, 4, 4, 2, 2, 3, 1, 5, 1, 2, 1, 3, 3, 3,
#               4, 1, 1, 5, 1, 3, 2, 4, 1, 5, 5, 1, 4, 4, 1, 4, 4, 1, 1, 2])

print(f'current state : {curr_state} \n')
for i in range(1, 81):
    print(i)
    curr_state -= 1
    count = 0
    count = np.count_nonzero(curr_state == -1)
    curr_state = np.where(curr_state == -1, 6, curr_state)
    if count > 0:
        new = np.array([8]*count)
        curr_state = np.append(curr_state, new)
    # print(f'day{i} state = {curr_state}')
print(len(curr_state))

# for i in range(1, 257):
#     print(i)
#     temp_state = []
#     curr_state -= 1
#     count = 0
#     for j in curr_state:
#         if j == -1:
#             j = 6
#             count += 1
#         temp_state.append(j)
#     if count > 0:
#         for k in range(0, count):
#             temp_state.append(8)
#     curr_state = temp_state
#     # print(f'state after day {i} : {curr_state} \n')
#
# print(len(curr_state))






# print(bingo_board)

# num_lst = [92, 12, 94, 64, 14, 4, 99, 71, 47, 59, 37, 73, 29, 7, 16, 32, 40, 53, 30, 76, 74, 39, 70, 88, 55, 45, 17, 0,
#            24, 65, 35, 20, 63, 68, 89, 84, 33, 66, 18, 50, 38, 10, 83, 75, 67, 42, 3, 56, 82, 34, 90, 46, 87, 52, 49, 2,
#            21, 62, 93, 86, 25, 78, 19, 57, 77, 26, 81, 15, 23, 31, 54, 48, 98,
#            11, 91, 85, 60, 72, 8, 69, 6, 22, 97, 96, 80, 95, 58, 36, 44, 1, 51, 43, 9, 61, 41, 79, 5, 27, 28, 13]
#
# for num_index, num in enumerate(num_lst):
#     flag = False
#     updated_board = []
#     for index, board in enumerate(bingo_board):
#         new_rows = board.dropna(axis=0, how='all').shape[0]
#         new_cols = board.dropna(axis=1, how='all').shape[1]
#         if (new_rows != board.shape[0]) | (new_cols != board.shape[1]):
#             board_sum = board.sum().sum()
#             final_score = board_sum * num_lst[num_index-1]
#             print(f"Final score = {final_score} = {board_sum} * {num_lst[num_index-1]}")
#             # print(board)
#             # flag = True
#             # break
#         else:
#             board = board.replace(num, np.nan)
#             updated_board.append(board)
#
#     bingo_board = updated_board
#
