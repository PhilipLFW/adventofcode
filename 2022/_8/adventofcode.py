import pandas as pd
import numpy as np
import os

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('/')[-1]
data = np.genfromtxt(file, dtype=int, comments='|||', delimiter=1)

##a
rows, cols = data.shape
visible = np.zeros_like(data)
for x in range(rows):
    for y in range(cols):
        height = data[x, y]

        # check if a tree is on the edge
        _edge = (x == 0 or y == 0 or x == rows - 1 or y == rows - 1)

        # check if all trees on a particular side are smaller
        _left = np.all(data[x, :y] < height)
        _right = np.all(data[x, y + 1:] < height)
        _top = np.all(data[:x, y] < height)
        _bottom = np.all(data[x + 1:, y] < height)

        # visible if one of above holds
        if _top or _left or _bottom or _right or _edge:
            visible[x, y] = 1

ans_a = np.sum(visible)

##b
scenic_score = np.ones_like(data)
for x in range(rows):
    for y in range(cols):
        if x == 0 or y == 0 or x == rows - 1 or y == cols - 1:
            scenic_score[x, y] = 0
            continue
        
        # start from tree
        height = data[x, y]

        # how far can we see down
        score = 0
        for i in range(x + 1, rows):
            score += 1
            if data[i, y] >= height or i == rows - 1:
                scenic_score[x, y] *= score
                break

        # how far can we see up
        score = 0
        for i in range(x - 1, -1, -1):
            score += 1
            if data[i, y] >= height or i == 0:
                scenic_score[x, y] *= score
                break

        # how far can we see left
        score = 0
        for j in range(y - 1, -1, -1):
            score += 1
            if data[x, j] >= height or j == 0:
                scenic_score[x, y] *= score
                break

        # how far can we see right
        score = 0
        for j in range(y + 1, cols):
            score += 1
            if data[x, j] >= height or j == cols - 1:
                scenic_score[x, y] *= score
                break

ans_b = np.max(scenic_score)

if __name__ == "__main__":
    print(f'Answer {day[-1]}a:', ans_a)
    print(f'Answer {day[-1]}b:', ans_b)
