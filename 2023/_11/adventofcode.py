import pandas as pd
import numpy as np
import os

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('_')[-2]
data = np.genfromtxt(file, delimiter=1, dtype=str, comments=None)

expand_rows = (data=='.').all(axis=1)
expand_cols = (data=='.').all(axis=0)

# initial part 1 solve
# data = np.repeat(data, 1 + expand_rows * 1, axis = 0)
# data = np.repeat(data, 1 + expand_cols * 1, axis = 1)

def get_total_distance(incr=2):
    locs = {i: (x, y) for i, (x, y) in enumerate(np.argwhere(data == '#'))}
    dists = []
    for galaxy1, pos1 in locs.items():
        for galaxy2, pos2 in locs.items():
            dist = 0
            if galaxy2 > galaxy1:
                for i in range(pos1[0], pos2[0], 1 if pos2[0] > pos1[0] else -1):
                    dist += 1 + expand_rows[i] * (incr - 1)
                for j in range(pos1[1], pos2[1], 1 if pos2[1] > pos1[1] else -1):
                    dist += 1 + expand_cols[j] * (incr - 1)
                dists += [dist]
    return sum(dists)


##a
ans_a = get_total_distance()

##b
ans_b = get_total_distance(1000000)

if __name__ == "__main__":
    print(f'Answer {day}a:', ans_a)
    print(f'Answer {day}b:', ans_b)
