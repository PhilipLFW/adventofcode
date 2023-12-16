import pandas as pd
import numpy as np
import os

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('_')[-2]
with open(file, 'r') as f:
    data = [txt.replace('\n', '') for txt in f.readlines()]

##a
times = [int(x) for x in data[0].split()[1:]]
distances = [int(x) for x in data[1].split()[1:]]

boat_distance = lambda time, button: (time - button) * button

def beat_the_race(times, distances):
    score = 1
    for t, d in zip(times, distances):
        score *= sum([boat_distance(t, x) > d for x in range(t)])
    return score

ans_a = beat_the_race(times, distances)

##b
ans_b = beat_the_race([int(''.join([str(t) for t in times]))], [int(''.join([str(d) for d in distances]))])

if __name__ == "__main__":
    print(f'Answer {day}a:', ans_a)
    print(f'Answer {day}b:', ans_b)
