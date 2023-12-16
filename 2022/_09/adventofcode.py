import pandas as pd
import numpy as np
import os

TESTING = False

file = 'test_a.txt' if TESTING else 'input.txt'
day = os.getcwd().split('/')[-1]
with open(file, 'r') as f:
    data = [txt.replace('\n', '') for txt in f.readlines()]

file = 'test_b.txt' if TESTING else 'input.txt'
with open(file, 'r') as f:
    data_b = [txt.replace('\n', '') for txt in f.readlines()]


def print_image(df):
    """use for testing"""
    print(str(df).replace(' [', '').replace('[', '').replace(']', '').replace('\n  ', ' ').replace('\'', '') + '\n')

directions = {'R': np.array([0, 1]), 'U': np.array([-1, 0]), 'D': np.array([1, 0]), 'L': np.array([0, -1])}

##a
T_visited = {(0, 0)}
T_loc = np.array([0, 0])
H_loc = np.array([0, 0])

for direction in data:
    orient, steps = direction.split()
    for _ in range(int(steps)):
        H_loc += directions[orient]
        if max(abs((H_loc - T_loc))) > 1:
            T_loc = H_loc - directions[orient]
            T_visited |= {tuple(T_loc)}

ans_a = len(T_visited)

##b
T_visited = {(0, 0)}
locs = {k: np.array([0, 0]) for k in range(10)}
data = data_b.copy()

for direction in data:
    change_direction = False
    orient, steps = direction.split()
    for i in range(int(steps)):
        locs[0] += directions[orient]
        for j in range(1, 10):
            if max(abs((locs[j] - locs[j - 1]))) > 1:
                step = np.clip(locs[j-1] - locs[j], -1, 1)
                locs[j] = locs[j] + step
            # grid = np.full_like(np.ones((30, 30)), '.', dtype=str)
            # grid[15, 15] = 's'
            # for k, v in list(locs.items())[::-1]:
            #     grid[v[0] + 15, v[1] + 15] = k
        T_visited |= {tuple(locs[9])}
        # print_image(grid)
    # print_image(grid)

ans_b = len(T_visited)

if __name__ == "__main__":
    print(f'Answer {day[-1]}a:', ans_a)
    print(f'Answer {day[-1]}b:', ans_b)
