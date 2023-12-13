import pandas as pd
import numpy as np
import os

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('_')[-2]
with open(file, 'r') as f:
    data = [txt.replace('\n', '') for txt in f.readlines()]

newlines = [i for i, x in enumerate(data) if x == ''] + [len(data)]
grids = []
curr = 0
for i in newlines:
    grids += [np.array([np.array(list(g)) for g in data[curr:i]])]
    curr = i + 1

def get_mirror_score(imperfections=0):
    score = 0
    for g, grid in enumerate(grids):

        for j in range(grid.shape[1]):
            left = grid[:, :j]
            right = grid[:, j:][:, ::-1]
            if left.shape[1] > right.shape[1]:
                left = left[:, -right.shape[1]:]
            else:
                right = right[:, -left.shape[1]:]
            if left.size and right.size and np.sum(left != right) == imperfections:
                score += j
                print(f'grid {g}: between column {j} and {j+1}')
                break
        for i in range(grid.shape[0]):
            up = grid[:i, :]
            down = grid[i:, :][::-1, :]
            if up.shape[0] > down.shape[0]:
                up = up[-down.shape[0]:, :]
            else:
                down = down[-up.shape[0]:, :]
            if up.size and down.size and np.sum(up != down) == imperfections:
                score += i * 100
                print(f'grid {i}: between row {i} and {i+1}')
                break
    return score

##a
ans_a = get_mirror_score(0)

##b
ans_b = get_mirror_score(1)

if __name__ == "__main__":
    print(f'Answer {day}a:', ans_a)
    print(f'Answer {day}b:', ans_b)
