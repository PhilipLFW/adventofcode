import pandas as pd
import numpy as np
import os
from collections import defaultdict

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('/')[-2]
with open(file, 'r') as f:
    data = [txt.replace('\n', '') for txt in f.readlines()]


def compare_pairs(left, right, parent_left=None, parent_right=None, grandparent_left=None, grandparent_right=None, level=0):
    if not parent_left and not parent_right:
        parent_left = grandparent_left
        parent_right = grandparent_right
        if parent_left or parent_right:
            level -= 1

    if not left and not right:
        left = parent_left
        right = parent_right
        level -= 1

    if not left and right:
        print('    ' * level, 'Left side ran out of items, so inputs are in the right order')
        return True
    elif left and not right:
        print('    ' * level, 'Right side ran out of items, so inputs are not in the right order')
        return False

    l, r = left.pop(0), right.pop(0)
    print('    ' * level, 'Compare:', l, 'vs', r)

    if isinstance(l, int) & isinstance(r, int):
        if l < r:
            print('    ' * (level + 1), 'Left side is smaller, so inputs are in the right order')
            return True
        elif l == r:
            return compare_pairs(left, right, parent_left, parent_right, level=level)
        else:
            print('    ' * (level + 1), 'Right side is smaller, so inputs are not in the right order')
            return False
    if isinstance(l, list) & isinstance(r, list):
        if not l and r:
            print('    ' * (level + 1), 'Left side ran out of items, so inputs are in the right order')
            return True
        elif l and r:
            return compare_pairs(l, r, left, right, parent_left, parent_right, level=level+1)
        elif not l and not r:
            return compare_pairs(left, right, parent_left, parent_right, level=level)
        else:
            print('    ' * (level + 1), 'Right side ran out of items, so inputs are not in the right order')
            return False
    if isinstance(l, list) & isinstance(r, int):
        print('    ' * level, f'Mixed types; convert right to {[r]} and retry comparison')
        print('    ' * level, 'Compare:', l, 'vs', [r])
        return compare_pairs(l, [r], left, right, parent_left, parent_right, level=level+1)
    if isinstance(l, int) & isinstance(r, list):
        print('    ' * level, f'Mixed types; convert left to {[l]} and retry comparison')
        print('    ' * level, 'Compare:', [l], 'vs', r)
        return compare_pairs([l], r, left, right, parent_left, parent_right, level=level+1)



##a
res = []
for i in range((len(data) + 1) // 3):
    print(f'== Pair {i + 1} ==')
    pairs = data[i*3:(i+1)*3]
    left = eval(pairs[0])
    right = eval(pairs[1])
    print('Compare:', left, 'vs', right)
    if compare_pairs(left, right):
        res += [i+1]
    print('\n')

ans_a = sum(res)

##b
res = {0: 1, 1: 2}
for j in range(2):
    for i in range((len(data))):
        if data[i]:
            print(f'== Packet {i + 1} ==')
            left = eval(data[i])
            right = [[2]] if not j else [[6]]
            print('Compare:', left, 'vs', right)
            if compare_pairs(left, right):
                res[j] += 1
            print('\n')

ans_b = np.prod([x for x in res.values()])

if __name__ == "__main__":
    print(f'Answer {day[-2]}a:', ans_a)
    print(f'Answer {day[-2]}b:', ans_b)
