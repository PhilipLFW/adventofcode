import pandas as pd
import numpy as np
import os
from collections import defaultdict

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('/')[-2]
with open(file, 'r') as f:
    data = [txt.replace('\n', '') for txt in f.readlines()]


def compare_pairs(l, r, level=0):
    print('    ' * level, 'Compare:', l, 'vs', r)

    if isinstance(l, int) & isinstance(r, int):
        if l < r:
            print('    ' * (level + 1), 'Left side is smaller, so inputs are in the right order')
            return True
        elif l > r:
            print('    ' * (level + 1), 'Right side is smaller, so inputs are not in the right order')
            return False
    if isinstance(l, list) & isinstance(r, list):
        for result in map(compare_pairs, l, r, [level + 1] * 100):
            if result is not None:
                return result
        if len(l) < len(r):
            print('    ' * (level + 1), 'Left side ran out of items, so inputs are in the right order')
            return True
        elif len(l) > len(r):
            print('    ' * (level + 1), 'Right side ran out of items, so inputs are not in the right order')
            return False
    if isinstance(l, list) & isinstance(r, int):
        print('    ' * level, f'Mixed types; convert right to {[r]} and retry comparison')
        print('    ' * level, 'Compare:', l, 'vs', [r])
        return compare_pairs(l, [r], level+1)
    if isinstance(l, int) & isinstance(r, list):
        print('    ' * level, f'Mixed types; convert left to {[l]} and retry comparison')
        print('    ' * level, 'Compare:', [l], 'vs', r)
        return compare_pairs([l], r, level+1)


##a
res = []
for i in range((len(data) + 1) // 3):
    print(f'== Pair {i + 1} ==')
    pairs = data[i*3:(i+1)*3]
    left = eval(pairs[0])
    right = eval(pairs[1])
    if compare_pairs(left, right):
        res += [i+1]
    print('\n')

ans_a = sum(res)


##b
sort_packets = sorted([x.replace('[', '').replace(']', '').replace('10', 'X') for x in data + ['[[2]]', '[[6]]'] if x])
dividers = [sort_packets.index('2') + 1, sort_packets.index('6') + 1]

ans_b = np.prod(dividers)


if __name__ == "__main__":
    print(f'Answer {day[-2]}a:', ans_a)
    print(f'Answer {day[-2]}b:', ans_b)
