import pandas as pd
import numpy as np
import os

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('/')[-2]
with open(file, 'r') as f:
    data = [txt.replace('\n', '') for txt in f.readlines()]


def add_crt(i, reg, result, command, num=None):
    n = 1 if command == 'noop' else 2
    for j in range(n):
        x = i % 40
        y = i // 40
        result[y, x] = '#' if abs(reg - x) <= 1 else '.'
        i += 1
    reg += int(num) if num else 0
    return i, reg, result


def add_result(i, reg, result, command, num=None):
    n = 1 if command == 'noop' else 2
    for j in range(n):
        i += 1
        if not (i - 20) % 40:
            result += [reg * i]
    reg += int(num) if num else 0
    return i, reg, result


def print_image(df):
    """use for testing"""
    print(str(df).replace(' [', '').replace('[', '').replace(']', '').replace('\n  ', ' ').replace('\'', '') + '\n')


##a
X = 1
i = 0
result = []
for instr in data:
    if instr == 'noop':
        i, X, result = add_result(i, X, result, 'noop')
    else:
        command, num = instr.split()
        i, X, result = add_result(i, X, result, command, num)

ans_a = sum(result)

##b
X = 1
i = 0
result = np.empty_like(np.zeros((6, 40)), dtype=str)
for instr in data:
    if instr == 'noop':
        i, X, result = add_crt(i, X, result, 'noop')
    else:
        command, num = instr.split()
        i, X, result = add_crt(i, X, result, command, num)

print_image(result)
ans_b = None

if __name__ == "__main__":
    print(f'Answer {day[-2]}a:', ans_a)
    print(f'Answer {day[-2]}b:', ans_b)
