import numpy as np
from scipy.sparse import csr_matrix, lil_matrix
from scipy.sparse.csgraph import shortest_path

grid = np.genfromtxt("day15/adventofcode15.txt", delimiter=1, dtype=int)

def get_distance_graph(grid):
    rows, cols = grid.shape
    dists = lil_matrix((rows*cols, rows*cols))
    adj = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for h in range(rows):
        for v in range(cols):
            for i, j in adj:
                if 0 <= (h + i) < rows and 0 <= (v + j) < cols:
                    dists[h * rows + v, (h + i) * rows + (v + j)] = grid[h + i, v + j]
    return csr_matrix(dists)

graph = get_distance_graph(grid)
dist = shortest_path(graph, directed=True, indices=0)  # shortest path from (0,0) to any point on the grid

## 15a
ans_15a = dist[-1]

## 15b
tiles = np.tile(np.repeat([0,1,2,3,4], grid.shape[0]), (grid.shape[0]*5, 1))
new_grid = (np.tile(grid, (5,5)) + tiles + tiles.T - 1) % 9 + 1
graph = get_distance_graph(new_grid)
dist = shortest_path(graph, directed=True, indices=0)  # shortest path from (0,0) to any point on the grid
ans_15b = dist[-1]

if __name__ == "__main__":
    print('Answer 15a:', ans_15a)
    print('Answer 15b:', ans_15b)
