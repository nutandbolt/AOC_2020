import pandas as pd
import numpy as np

'''
https://adventofcode.com/2021/day/5

'''

# Part 1
file_loc = r'aoc_5_input.txt'
hydro_df = pd.DataFrame(columns=['X', 'Y', 'count'])
vent_lst = []
count_lst = []
with open(file_loc, 'r') as fp:
    for line in fp:
        line = line.strip()
        X1, Y1 = line.split('->')[0].strip().split(',')
        X2, Y2 = line.split('->')[1].strip().split(',')

        if X1 == X2:
            if int(Y1) > int(Y2) :
                start_y = int(Y2)
                end_y = int(Y1)
            else:
                start_y = int(Y1)
                end_y = int(Y2)

            for i in range(start_y, end_y+1):
                if (int(X1), i) not in vent_lst:
                    vent_lst.append((int(X1), i))
                    count_lst.append(1)
                else:
                    repeat_index = vent_lst.index((int(X1), i))
                    count_lst[repeat_index] += 1
        elif Y1 == Y2:
            if int(X1) > int(X2):
                start_x = int(X2)
                end_x = int(X1)
            else:
                start_x = int(X1)
                end_x = int(X2)

            for i in range(start_x, end_x + 1):
                if (i, int(Y1)) not in vent_lst:
                    vent_lst.append((i, int(Y1)))
                    count_lst.append(1)
                else:
                    repeat_index = vent_lst.index((i, int(Y1)))
                    count_lst[repeat_index] += 1
        else:
            start_x = int(X1)
            end_x = int(X2)
            start_y = int(Y1)
            end_y = int(Y2)

            if start_x > end_x:
                inc_x = -1
                end_x -= 1
            else:
                inc_x = 1
                end_x += 1
            if start_y > end_y:
                inc_y = -1
                end_y -= 1
            else:
                inc_y = 1
                end_y += 1

            for i, j in zip(range(start_x, end_x, inc_x), range(start_y, end_y, inc_y)):
                if(i, j) not in vent_lst:
                    vent_lst.append((i, j))
                    count_lst.append(1)
                else:
                    repeat_index = vent_lst.index((i, j))
                    count_lst[repeat_index] += 1

print(sum(map(lambda x: x > 1, count_lst)))
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
