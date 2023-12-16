import functools

import pandas as pd
import numpy as np
import os
from itertools import product
from functools import cache
from collections import Counter

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('_')[-2]
with open(file, 'r') as f:
    data = [txt.replace('\n', '') for txt in f.readlines()]

springs = [x.split()[0] for x in data]
orders = [x.split()[1] for x in data]

@cache
def rep_spring(spring, order, cut='', cut_order=''):
    # print(cut + '  ' + spring, '\t', cut_order + '  ' + order)
    if not '?' in spring:
        if order and len(order.split(',')) == 1 and Counter(spring)['#'] == int(order) and int(order) * '#' in spring:
            # print(cut + '  ' + spring, '\t', cut_order + '  ' + order, 'YIELD')
            return 1
        elif not order and not spring.replace('.', ''):
            # print(cut + '  ' + spring, '\t', cut_order + '  ' + order, 'YIELD')
            return 1
        elif ','.join([str(len(x)) for x in spring.replace('.', ' ').split()]) == order:
            # print(cut + '  ' + spring, '\t', cut_order + '  ' + order, 'YIELD')
            return 1
        else:
            # print(cut + '  ' + spring, '\t', cut_order + '  ' + order, 'BREAK')
            return 0
    elif order or (not order and not '#' in spring):
        ss = spring.replace('.', ' ').split()
        hash_length = Counter(ss[0])['#']
        desired_hash_lengths = order.split(',') if order else ['0']
        if (not '?' in ss[0] and hash_length != int(desired_hash_lengths[0])) or (int(desired_hash_lengths[0]) + 1) * '#' in ss[0].split('?')[0]:
            # print(cut + '  ' + spring, '\t', cut_order + '  ' + order, 'BREAK')
            return 0
        elif not '?' in ss[0] and ss[0] == '#' * int(desired_hash_lengths[0]):
            cut += ss[0] + '.'
            spring = '.'.join(ss[1:])
            cut_order += desired_hash_lengths[0] + ','
            order = ','.join(desired_hash_lengths[1:])
        spring_hash = rep_spring(spring.replace('?', '#', 1), order, cut, cut_order)
        spring_dot = rep_spring(spring.replace('?', '.', 1), order, cut, cut_order)

        res = 0
        res += spring_hash
        res += spring_dot

        return res

    else:
        return 0

##a
score = 0
for i, (spring, order) in enumerate(zip(springs, orders)):
    print(f'{i + 1} / {len(orders)}')
    arrangements = rep_spring(spring, order)
    print(f'Total score: {arrangements}')
    score += arrangements

ans_a = score


## b
springs = ['?'.join([s] * 5) for s in springs]
orders = [','.join([o] * 5) for o in orders]

score = 0
for i, (spring, order) in enumerate(zip(springs, orders)):
    print(f'{i + 1} / {len(orders)}')
    arrangements = rep_spring(spring, order)
    print(f'Total score: {arrangements}')
    score += arrangements

ans_b = score


if __name__ == "__main__":
    print(f'Answer {day}a:', ans_a)
    print(f'Answer {day}b:', ans_b)
