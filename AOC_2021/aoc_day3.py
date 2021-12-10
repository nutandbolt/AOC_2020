import pandas as pd
import numpy as np

'''
https://adventofcode.com/2021/day/3

'''

# Part 1



file_loc = r'aoc_3_input.txt'
main_df = pd.DataFrame(columns=range(0, 13))

with open(file_loc, 'r') as fp:
    for line in fp:
        temp_df = pd.DataFrame([list(line)])
        main_df = main_df.merge(temp_df, how="outer")

gamma_rate = []
epsilon_rate = []

for i in range(0, 12):
    zero_count = main_df[i].value_counts(sort=False)[0]
    one_count = main_df[i].value_counts(sort=False)[1]

    if zero_count > one_count:
        gamma = 0
        epsilon = 1
    else:
        gamma = 1
        epsilon = 0

    gamma_rate.append(gamma)
    epsilon_rate.append(epsilon)

gamma_dec = 0
epsilon_dec = 0

for index, i in enumerate(gamma_rate[::-1]):
    gamma_dec += i*pow(2, index)

for index, i in enumerate(epsilon_rate[::-1]):
    epsilon_dec += i*pow(2, index)


print(gamma_dec * epsilon_dec)

# part 2
check_df = main_df.copy()

for i in range(0, 12):
    zero_count = check_df[i].value_counts(sort=False).loc['0']
    one_count = check_df[i].value_counts(sort=False).loc['1']

    if zero_count > one_count:

        o2_df = (check_df.loc[check_df[i] == '0', :]).reset_index(drop=True)
        co2_df = (check_df.loc[check_df[i] == '1', :]).reset_index(drop=True)

    else:

        o2_df = (check_df.loc[check_df[i] == '1', :]).reset_index(drop=True)
        co2_df = (check_df.loc[check_df[i] == '0', :]).reset_index(drop=True)

    if len(co2_df) == 1:
        break
    else:
        # check_df = o2_df.copy()
        check_df = co2_df.copy()

print(co2_df)


