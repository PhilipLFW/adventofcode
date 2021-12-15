import numpy as np
from scipy.sparse import csr_matrix, lil_matrix
from scipy.sparse.csgraph import shortest_path

with open('day15/adventofcode15.txt', 'r') as f:
    raw = f.readlines()
    grid = np.array([[int(char) for char in chars]
              for chars in [list(line)
                            for line in [txt.replace('\n', '')
                                         for txt in raw]]])
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
new_grid = (np.concatenate((np.concatenate((grid, grid+1, grid+2, grid+3, grid+4)),
np.concatenate((grid+1, grid+2, grid+3, grid+4, grid+5)),
np.concatenate((grid+2, grid+3, grid+4, grid+5, grid+6)),
np.concatenate((grid+3, grid+4, grid+5, grid+6, grid+7)),
np.concatenate((grid+4, grid+5, grid+6, grid+7, grid+8))), axis=1) - 1) % 9 + 1
graph = get_distance_graph(new_grid)
dist = shortest_path(graph, directed=True, indices=0)  # shortest path from (0,0) to any point on the grid
ans_15b = dist[-1]

if __name__ == "__main__":
    print('Answer 15a:', ans_15a)
    print('Answer 15b:', ans_15b)
