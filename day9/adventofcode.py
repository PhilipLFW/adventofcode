import pandas as pd
import numpy as np

with open('day9/adventofcode9.txt', 'r') as f:
    raw = f.readlines()
    data = ['9' + txt.replace('\n', '') + '9' for txt in raw]
    data.insert(0, '9' * len(data[0]))
    data.append('9' * len(data[-1]))

## 9a
risk = 0
low_points = []
for i in range(1,len(data)-1):
    for j in range(1,len(data[0])-1):
        point = data[i][j]
        print(point)
        adjacent_points = [data[i][j+1], data[i+1][j], data[i-1][j], data[i][j-1]]
        print(adjacent_points)
        if all([point < adj for adj in adjacent_points]):
            print('low point!')
            low_points += [(i, j)]
            risk += 1 + int(point)
ans_9a = risk

## 9b
explore_data = data.copy()
basin_sizes_dict = {p: [] for p in low_points}
for point in low_points:
    this_basin = {point}
    print('Low point:', this_basin)
    still_growing = True
    while still_growing:
        basin_size = len(this_basin)
        for p in this_basin:
            i, j = p
            adj_points = [(i, j+1), (i+1, j), (i-1, j), (i, j-1)]
            for c_i, c_j in adj_points:
                if explore_data[c_i][c_j] != '9':
                    this_basin = this_basin.union({(c_i, c_j)})
        print('Exploring...:', this_basin, len(this_basin))
        if basin_size == len(this_basin):
            print('We have explored the basin!')
            still_growing = False
    basin_sizes_dict[point] = len(this_basin)
basin_sizes = np.array(list(basin_sizes_dict.values()))
ans_9b = basin_sizes[np.argsort(basin_sizes)[-3:]].prod()

if __name__ == "__main__":
    print('Answer 9a:', ans_9a)
    print('Answer 9b:', ans_9b)
