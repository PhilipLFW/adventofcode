import pandas as pd
import numpy as np
import os

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('/')[-1]
data = np.genfromtxt(file, dtype=int, delimiter=1)

##a
rows, cols = data.shape
visible = np.zeros_like(data)
for x in range(rows):
    for y in range(cols):
        height = data[x, y]

        # check if all trees on a particular side are smaller
        _left = np.all(data[x, :y] < height)
        _right = np.all(data[x, y + 1:] < height)
        _top = np.all(data[:x, y] < height)
        _bottom = np.all(data[x + 1:, y] < height)

        # visible if one of above holds
        if _top or _left or _bottom or _right:
            visible[x, y] = 1

ans_a = np.sum(visible)

##b
scenic_score = np.ones_like(data)
for x in range(rows):
    for y in range(cols):
        if x == 0 or y == 0 or x == rows - 1 or y == cols - 1:
            scenic_score[x, y] = 0
            continue

        # start from tree, go right (0,1), down (1,0), left (0,-1) and up (-1, 0)
        height = data[x, y]
        lower = data < data[x, y]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for direction in directions:
            i, j = np.array((x, y)) + np.array(direction)
            score = 1
            while lower[i, j] and 0 < i < rows-1 and 0 < j < cols-1:
                i, j = np.array((i, j)) + np.array(direction)
                score += 1
            scenic_score[x, y] *= score

ans_b = np.max(scenic_score)

if __name__ == "__main__":
    print(f'Answer {day[-1]}a:', ans_a)
    print(f'Answer {day[-1]}b:', ans_b)
