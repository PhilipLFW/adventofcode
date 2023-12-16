import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

with open('day13/adventofcode13.txt', 'r') as f:
    raw = f.readlines()
    dots = [txt.replace('\n', '') for txt in raw]

folds = """fold along x=655
fold along y=447
fold along x=327
fold along y=223
fold along x=163
fold along y=111
fold along x=81
fold along y=55
fold along x=40
fold along y=27
fold along y=13
fold along y=6""".replace('fold along ', '').split('\n')

dims = max([eval(dot)[1] for dot in dots]) + 1, max([eval(dot)[0] for dot in dots]) + 1
grid = np.zeros(dims)
for dot in dots:
    y, x = eval(dot)
    grid[x, y] += 1

def apply_fold(grid, fold):
    ax, line = fold.split('=')
    if ax == 'y':
        new_grid = grid[:int(line)] + grid[:int(line):-1]
    else:
        new_grid = grid[:,:int(line)] + grid[:,:int(line):-1]
    return new_grid

## 13a
grid_a = grid.copy()
grid_a = apply_fold(grid_a, folds[0])
ans_13a = sum(sum(grid_a>0))

## 13b
grid_b = grid.copy()
for fold in folds:
    grid_b = apply_fold(grid_b, fold)

plt.clf()
for x in range(grid_b.shape[0]):
    for y in range(grid_b.shape[1]):
        if grid_b[x,y] > 0:
            plt.scatter(y, grid_b.shape[0]-x, marker='s', s=1200, c='black')
fig = plt.gcf()
fig.set_size_inches(grid_b.shape[1]/2, grid_b.shape[0]/2)
fig.savefig('day13/ans_13b.png')
ans_13b = "SEE FIGURE!!"

if __name__ == "__main__":
    print('Answer 13a:', ans_13a)
    print('Answer 13b:', ans_13b)
