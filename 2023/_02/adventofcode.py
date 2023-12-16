import pandas as pd
import numpy as np
import os

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('/')[-2]
with open(file, 'r') as f:
    data = [txt.replace('\n', '') for txt in f.readlines()]

max_cubes = {'red': 12,
             'green': 13,
             'blue': 14}

games = {int(x.split(': ')[0].split(' ')[1]): x.split(': ')[1].split('; ') for x in data}
all_games = {}
maxima = {}

for g, hands in games.items():
    all_games[g] = {}
    maxima[g] = {}
    for i, hand in enumerate(hands):
        all_games[g][i] = {}
        h = {'red': 0, 'green': 0, 'blue': 0}
        for color in hand.split(', '):
            n, c = color.split(' ')
            h[c] = n
        all_games[g][i] = h
    for rgb in ['red', 'green', 'blue']:
        maxima[g][rgb] = max([int(all_games[g][i][rgb]) for i in all_games[g]])


##a
score = 0
for g, m in maxima.items():
    if m['red'] <= 12 and m['green'] <= 13 and m['blue'] <= 14:
        score += g
ans_a = score

##b
score = 0
for g, m in maxima.items():
    power = m['red'] * m['green'] * m['blue']
    score += power
ans_b = score

if __name__ == "__main__":
    print(f'Answer {day[-2]}a:', ans_a)
    print(f'Answer {day[-2]}b:', ans_b)
