import pandas as pd
import numpy as np

'''
https://adventofcode.com/2021/day/6

'''

# Part 1/2

# curr_state = np.array([3, 4, 3, 1, 2])
curr_state = np.array([1, 1, 1, 3, 3, 2, 1, 1, 1, 1, 1, 4, 4, 1, 4, 1, 4, 1, 1, 4, 1, 1, 1, 3, 3, 2, 3, 1, 2, 1, 1, 1,
              1, 1, 1,
              1, 3, 4, 1, 1, 4, 3, 1, 2, 3, 1, 1, 1, 5, 2, 1, 1, 1, 1, 2, 1, 2, 5, 2, 2, 1, 1, 1, 3, 1, 1, 1, 4, 1, 1,
              1, 1, 1, 3, 3, 2, 1, 1, 3, 1, 4, 1, 2, 1, 5, 1, 4, 2, 1, 1, 5, 1, 1, 1, 1, 4, 3, 1, 3, 2, 1, 4, 1, 1, 2,
              1, 4, 4, 5, 1, 3, 1, 1, 1, 1, 2, 1, 4, 4, 1, 1, 1, 3, 1, 5, 1, 1, 1, 1, 1, 3, 2, 5, 1, 5, 4, 1, 4, 1, 3,
              5, 1, 2, 5, 4, 3, 3, 2, 4, 1, 5, 1, 1, 2, 4, 1, 1, 1, 1, 2, 4, 1, 2, 5, 1, 4, 1, 4, 2, 5, 4, 1, 1, 2, 2,
              4, 1, 5, 1, 4, 3, 3, 2, 3, 1, 2, 3, 1, 4, 1, 1, 1, 3, 5, 1, 1, 1, 3, 5, 1, 1, 4, 1, 4, 4, 1, 3, 1, 1, 1,
              2, 3, 3, 2, 5, 1, 2, 1, 1, 2, 2, 1, 3, 4, 1, 3, 5, 1, 3, 4, 3, 5, 1, 1, 5, 1, 3, 3, 2, 1, 5, 1, 1, 3, 1,
              1, 3, 1, 2, 1, 3, 2, 5, 1, 3, 1, 1, 3, 5, 1, 1, 1, 1, 2, 1, 2, 4, 4, 4, 2, 2, 3, 1, 5, 1, 2, 1, 3, 3, 3,
              4, 1, 1, 5, 1, 3, 2, 4, 1, 5, 5, 1, 4, 4, 1, 4, 4, 1, 1, 2])

count_state = np.zeros(9)
values, counts = np.unique(curr_state, return_counts=True)

for m, n in zip(values, counts):
    count_state[m] = n

print(f'current state : {curr_state} \n')
# count_state = [0, 1, 1, 2, 1, 0, 0, 0, 0]
for i in range(1, 257):
    print(i)
    temp_count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for j in range(1, 9):
        temp_count[j-1] = count_state[j]
    temp_count[6] += count_state[0]
    temp_count[8] = count_state[0]
    count_state = temp_count

print(sum(count_state))
