import pandas as pd
import numpy as np
import os
from collections import defaultdict, deque


TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('_')[-2]
data = np.genfromtxt(file, delimiter=1, dtype=int)


def shortest_path_restricted_a(data):
    data = data.copy()
    to_visit = deque([(0, 0, '')])
    dists = defaultdict(lambda: np.Inf)
    dists[(0, 0, '')] = 0
    paths = defaultdict(str)
    paths[(0, 0, '')] = str((0,0))
    directions = defaultdict(str)
    directions[(0, 0, '')] = ''
    while to_visit:
        curr = to_visit.popleft()
        curr_dist = dists[curr]
        curr_x, curr_y, curr_path = curr
        adj = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for d, (i, j) in enumerate(adj):
            direction = '><v^'[d]
            opposite = '<>^v'[d]
            if 0 <= curr_x + i < data.shape[0] and 0 <= curr_y + j < data.shape[1] and curr_path[-1:] != opposite:
                candidate = (curr_x + i, curr_y + j, curr_path[-2:] + direction)
                if curr_dist + data[candidate[0], candidate[1]] < dists[candidate] and curr_path[-3:] != direction * 3:
                    dists[candidate] = curr_dist + data[curr_x + i, curr_y + j]
                    paths[candidate] = paths[curr] + '-' + str((candidate[0], candidate[1]))
                    directions[candidate] = directions[curr] + direction
                    to_visit.append(candidate)
    return dists, paths, directions

##a
dists, paths, directions = shortest_path_restricted_a(data)
ans_a = min([v for k, v in dists.items() if k[0] == data.shape[0] - 1 and k[1] == data.shape[1] - 1])


def shortest_path_restricted_b(data):
    data = data.copy()
    to_visit = deque([(0, 0, 0, 1), (0, 0, 2, 1)])  # apparently the first element already counts as a step
    dists = defaultdict(lambda: np.Inf)
    dists[(0, 0, 0, 1)] = 0  # going right
    dists[(0, 0, 2, 1)] = 0  # going down
    while to_visit:
        curr = to_visit.popleft()
        curr_dist = dists[curr]
        curr_x, curr_y, curr_dir, curr_length = curr
        adj = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for d, (i, j) in enumerate(adj):
            if (curr_dir == 0 and d == 1) or (curr_dir == 1 and d == 0) or (curr_dir == 2 and d == 3) or (curr_dir == 3 and d == 2):
                continue
            if 0 <= curr_x + i < data.shape[0] and 0 <= curr_y + j < data.shape[1]:
                candidate = (curr_x + i, curr_y + j, d, curr_length + 1 if curr_dir == d else 1)
                if curr_dist + data[candidate[0], candidate[1]] < dists[candidate]:
                    if (curr_length < 4 and curr_dir == d) or 4 <= curr_length < 10 or (curr_length == 10 and curr_dir != d):
                        dists[candidate] = curr_dist + data[curr_x + i, curr_y + j]
                        to_visit.append(candidate)
    return dists

##b
dists = shortest_path_restricted_b(data)
ans_b = min([v for k, v in dists.items() if k[0] == data.shape[0] - 1 and k[1] == data.shape[1] - 1 and k[3] >= 4])


if __name__ == "__main__":
    print(f'Answer {day}a:', ans_a)
    print(f'Answer {day}b:', ans_b)
