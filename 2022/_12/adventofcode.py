import pandas as pd
import numpy as np
import os
from string import ascii_lowercase as letters
from scipy.sparse import csr_matrix, lil_matrix
from scipy.sparse.csgraph import shortest_path

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('/')[-2]
data = np.genfromtxt(file, delimiter=1, dtype=str)
grid = np.ones_like(data, dtype=int)
letters = 'S' + letters + 'E'


def get_distance_graph(grid):
    rows, cols = grid.shape
    dists = lil_matrix((rows*cols, rows*cols))
    adj = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for h, v in np.ndindex(data.shape):
        for i, j in adj:
            if 0 <= (h + i) < rows and 0 <= (v + j) < cols and \
                    letters.index(data[h + i, v + j].replace('E', 'z')) <= letters.index(data[h, v]) + 1:
                di = h * cols + v
                dj = (h+i) * cols + (v+j)
                dists[di, dj] += grid[h + i, v + j]
    return csr_matrix(dists)

##a
graph = get_distance_graph(grid)
dist = shortest_path(graph, indices=[i for i, x in enumerate(data.flatten()) if x == 'S'], directed=True)
ans_a = min(dist[:, data.flatten().tolist().index('E')])

##b
graph = get_distance_graph(grid)
dist = shortest_path(graph, indices=[i for i, x in enumerate(data.flatten()) if x == 'a' or x == 'S'], directed=True)
ans_b = min(dist[:, data.flatten().tolist().index('E')])

if __name__ == "__main__":
    print(f'Answer {day[-2]}a:', ans_a)
    print(f'Answer {day[-2]}b:', ans_b)
