import pandas as pd
import numpy as np
import os

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('_')[-2]
with open(file, 'r') as f:
    data = [txt.replace('\n', '') for txt in f.readlines()]

seqs = [[int(z) for z in x.split()] for x in data]

score = 0
for s in seqs:
    diffs = np.array(s)
    lasts = [s[-1]]
    while not all(diffs == 0):
        diffs = np.diff(diffs)
        lasts += [diffs[-1]]
    score += sum(lasts)


##a
ans_a = score


score = 0
for s in seqs:
    diffs = np.array(s)
    firsts = [s[0]]
    while not all(diffs == 0):
        diffs = np.diff(diffs)
        firsts += [diffs[0]]
    while len(firsts) > 1:
        firsts[-1] = firsts[-2] - firsts.pop(-1)
    score += firsts[0]


##b
ans_b = score

if __name__ == "__main__":
    print(f'Answer {day}a:', ans_a)
    print(f'Answer {day}b:', ans_b)
