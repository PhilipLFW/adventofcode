import pandas as pd
import numpy as np
import os

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('_')[-1]
data = np.genfromtxt(file, delimiter=1, dtype=str, comments=None)
data = np.pad(data, 1, 'constant', constant_values='.')

numbers = []
part_numbers = []
gears = {(x,y): [] for x, y in zip(*np.where(data == '*'))}

rows, cols = data.shape
current_num = ''
start_col = None
end_col = None
for i in range(rows):
    for j in range(cols):
        char = data[i, j]
        if char.isdigit():
            if not start_col:
                start_col = j
            current_num += char
        elif current_num:
            numbers += [int(current_num)]
            end_col = j-1
            current_num = ''
        else:
            continue
        if start_col and end_col:
            res = data[i-1:i+2, start_col-1:end_col+2].copy()
            res[1:-1, 1:-1] = '.' # replace the number
            if not np.all(res == '.'):
                part_numbers += [numbers[-1]]
            for r, c in np.ndindex(res.shape):
                if res[r, c] == '*':
                    gears[(i - 1 + r, start_col - 1 + c)] += [numbers[-1]]
            start_col = None
            end_col = None

##a
ans_a = sum(part_numbers)

##b
ans_b = sum([np.product(v) for k, v in gears.items() if len(v) == 2])

if __name__ == "__main__":
    print(f'Answer {day[-2]}a:', ans_a)
    print(f'Answer {day[-2]}b:', ans_b)
