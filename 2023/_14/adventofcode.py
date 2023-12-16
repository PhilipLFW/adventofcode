import pandas as pd
import numpy as np
import os
from functools import cache

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('_')[-2]
data = np.genfromtxt(file, delimiter=1, dtype=str, comments=None)
orig_data = data.copy()

def print_image(df):
    # for testing
    print(str(df).replace(' [', '').replace('[', '').replace(']', '').replace('\'', '') + '\n')


for x, y in np.argwhere(data == 'O'):
    data = np.rot90(data, 3)
    for i in range(x, 0, -1):
        if data[i-1, y] != '#' and data[i-1, y] != 'O':
            data[i, y] = '.'
            data[i-1, y] = 'O'
            # print_image(data)
        else:
            break

##a
ans_a = sum(data.shape[0] - np.where(data == 'O')[0])


@cache
def roll(O, R):
    data = empty_data.copy()
    for r in range(R + 1):
        data = np.rot90(data, 3)
    for o in O:
        data[o] = 'O'
    for x, y in np.argwhere(data == 'O'):
        for i in range(x, 0, -1):
            if data[i - 1, y] != '#' and data[i - 1, y] != 'O':
                data[i, y] = '.'
                data[i - 1, y] = 'O'
            else:
                break
    return data

data = np.rot90(orig_data.copy())
total = len(np.argwhere(orig_data == 'O'))
empty_data = orig_data.copy()
empty_data[np.where(empty_data == 'O')] = '.'
empty_data = np.rot90(empty_data)
all_coords = []
for _ in range(1000000000):
    for r in range(4):
        data = np.rot90(data, 3)
        coords = frozenset([tuple(x) for x in (np.argwhere(data == 'O'))])
        assert len(coords) == total
        data = roll(coords, r)
    orig_pos_data = np.rot90(data, 3)
    all_coords += [frozenset([tuple(x) for x in (np.argwhere(orig_pos_data == 'O'))])]
    # print_image(np.rot90(orig_pos_data, 3))
    if len(all_coords) > len(set(all_coords)):
        break

final = len(all_coords) - 1
start = all_coords.index(all_coords[final])
cycle = final - all_coords.index(all_coords[final])
iter = (1000000000 - start) % cycle

data = np.rot90(empty_data.copy(), 3)
for o in all_coords[start + iter - 1]:
    data[o] = 'O'


##b
ans_b = sum(data.shape[0] - np.where(data == 'O')[0])

if __name__ == "__main__":
    print(f'Answer {day}a:', ans_a)
    print(f'Answer {day}b:', ans_b)
