import numpy as np

input = np.array([[int(c) for c in line.strip()] for line in open('aoc_9_input.txt').readlines()], dtype=int)
input = np.pad(input, 1, 'constant', constant_values=9)


def findLowestPoints(array):
    lowest_points = []
    for y in range(1, input.shape[0] - 1):
        for x in range(1, input.shape[1] - 1):
            lowest = True
            for yy in range(y - 1, y + 2):
                for xx in range(x - 1, x + 2):
                    if input[y, x] > input[yy, xx]:
                        lowest = False

            if lowest:
                lowest_points.append((y, x))

    return lowest_points


# find lowest points
lowest_points = findLowestPoints(input)
print('Part #1:', sum(input[c] for c in lowest_points) + len(lowest_points))