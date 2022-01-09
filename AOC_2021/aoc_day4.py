import pandas as pd
import numpy as np

'''
https://adventofcode.com/2021/day/4

'''

# Part 1
file_loc = r'aoc_4_input.txt'
octo_df = pd.DataFrame(columns=range(0, 4))
bingo_board = []
with open(file_loc, 'r') as fp:
    for line in fp:
        line = line.strip()
        line = line.split(' ')
        line = [int(char) for char in line if char != '']
        if len(line) != 0:
            temp_df = pd.DataFrame([line])
            octo_df = octo_df.merge(temp_df, how="outer")
        else:
            bingo_board.append(octo_df)
            octo_df = pd.DataFrame(columns=range(0, 4))

# print(bingo_board)

num_lst = [92, 12, 94, 64, 14, 4, 99, 71, 47, 59, 37, 73, 29, 7, 16, 32, 40, 53, 30, 76, 74, 39, 70, 88, 55, 45, 17, 0,
           24, 65, 35, 20, 63, 68, 89, 84, 33, 66, 18, 50, 38, 10, 83, 75, 67, 42, 3, 56, 82, 34, 90, 46, 87, 52, 49, 2,
           21, 62, 93, 86, 25, 78, 19, 57, 77, 26, 81, 15, 23, 31, 54, 48, 98,
           11, 91, 85, 60, 72, 8, 69, 6, 22, 97, 96, 80, 95, 58, 36, 44, 1, 51, 43, 9, 61, 41, 79, 5, 27, 28, 13]

for num_index, num in enumerate(num_lst):
    flag = False
    updated_board = []
    for index, board in enumerate(bingo_board):
        new_rows = board.dropna(axis=0, how='all').shape[0]
        new_cols = board.dropna(axis=1, how='all').shape[1]
        if (new_rows != board.shape[0]) | (new_cols != board.shape[1]):
            board_sum = board.sum().sum()
            final_score = board_sum * num_lst[num_index-1]
            print(f"Final score = {final_score} = {board_sum} * {num_lst[num_index-1]}")
            # print(board)
            # flag = True
            # break
        else:
            board = board.replace(num, np.nan)
            updated_board.append(board)

    bingo_board = updated_board

