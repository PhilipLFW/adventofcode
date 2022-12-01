import pandas as pd
import numpy as np

with open('day06/adventofcode6.txt', 'r') as f:
    raw = f.readline()
    fish_init = [int(txt) for txt in raw.split(',')]

## 6a
days = 80
days_past = 0
fish_timers = fish_init.copy()
while days > 0:
    new_fish = 0
    for i, j in enumerate(fish_timers):
        if fish_timers[i] == 0:
            fish_timers[i] = 7
            new_fish += 1
        fish_timers[i] -= 1
    fish_timers += [8] * new_fish
    days -= 1
    days_past += 1
    print(f'{len(fish_timers)} after {days_past} days:')
          # , ','.join([str(k) for k in fish_timers]))

ans_6a = len(fish_timers)

## 6b
fish_records = {k: fish_init.count(k) for k in range(9)}
days = 256
days_past = 0
while days > 0:
    new_fish = fish_records[0]
    fish_records[7] = fish_records[7] + fish_records.pop(0)
    fish_records = {k - 1: v for k, v in fish_records.items()}
    fish_records[8] = new_fish
    days -= 1
    days_past += 1
    print(f'{sum([v for v in fish_records.values()])} after {days_past} days')

ans_6b = sum([v for v in fish_records.values()])

if __name__ == "__main__":
    print('Answer 6a:', ans_6a)
    print('Answer 6b:', ans_6b)
