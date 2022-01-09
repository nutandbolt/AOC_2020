import pandas as pd
import numpy as np

'''
https://adventofcode.com/2021/day/11

'''

# Part 1


def increase_energy(input_array, flashes):
    exp_octo = np.argwhere(input_array == 0)
    flashes += len(exp_octo)
    rows, cols = input_array.shape

    if len(exp_octo) == 0:
        return input_array, flashes

    for i, j in exp_octo:
        if j != cols-1:
            if (input_array[i][j+1] > 0) & (input_array[i][j+1] != 10):
                input_array[i][j+1] += 1
        if j != 0:
            if (input_array[i][j-1] > 0) & (input_array[i][j-1] != 10):
                input_array[i][j-1] += 1
        if i != rows-1:
            if (input_array[i + 1][j] > 0) & (input_array[i + 1][j] != 10):
                input_array[i + 1][j] += 1
        if i != 0:
            if (input_array[i - 1][j] > 0) & (input_array[i - 1][j] != 10):
                input_array[i - 1][j] += 1
        if (i != rows-1) & (j != cols-1):
            if (input_array[i+1][j+1] > 0) & (input_array[i+1][j+1] != 10):
                input_array[i + 1][j+1] += 1
        if (i != rows - 1) & (j != 0):
            if (input_array[i + 1][j - 1] > 0) & (input_array[i + 1][j - 1] != 10):
                input_array[i + 1][j - 1] += 1
        if (i != 0) & (j != cols - 1):
            if (input_array[i - 1][j + 1] > 0) & (input_array[i - 1][j + 1] != 10):
                input_array[i - 1][j + 1] += 1
        if (i != 0) & (j != 0):
            if (input_array[i - 1][j - 1] > 0) & (input_array[i - 1][j - 1] != 10):
                input_array[i - 1][j - 1] += 1
        input_array[i, j] = -1
    return increase_energy(np.where(input_array == 10, 0, input_array), flashes)


file_loc = r'aoc_11_input.txt'
octo_df = pd.DataFrame(columns=range(0, 10))
with open(file_loc, 'r') as fp:
    for line in fp:
        line = list(line.strip())
        temp_df = pd.DataFrame([line])
        octo_df = octo_df.merge(temp_df, how="outer")

octo_df = octo_df.astype(int)
octo_array = octo_df.to_numpy()
# octo_array = np.array([[5, 4,8,3,1,4,3,2,2,3],[2,7,4,5,8,5,4,7,1,1], [5,2,6,4,5,5,6,1,7,3],
#                        [6,1,4,1,3,3,6,1,4,6], [6,3,5,7,3,8,5,4,7,8], [4,1,6,7,5,2,4,6,4,5],
#                        [2,1,7,6,8,4,1,7,2,1],[6,8,8,2,8,8,1,1,3,4], [4,8,4,6,8,4,8,5,5,4],[5,2,8,3,7,5,1,5,2,6]])
end = 300
flash_count = 0

for i in range(0, end):
    octo_array += 1
    octo_array, flash_count = increase_energy(np.where(octo_array == 10, 0, octo_array), flash_count)
    octo_array = np.where(octo_array == -1, 0, octo_array)
    octo_flash_state_count = np.argwhere(octo_array == 0)
    if len(octo_flash_state_count) == 100:
        break

print(flash_count)
print(i+1)
