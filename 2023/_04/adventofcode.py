import pandas as pd
import numpy as np
import os

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('_')[-2]
with open(file, 'r') as f:
    data = [txt.replace('\n', '') for txt in f.readlines()]

cards = {int(x.split(': ')[0].split()[1]):
             {'winning': [int(z) for z in x.split(': ')[1].split(' | ')[0].split()],
              'mine': [int(z) for z in x.split(': ')[1].split(' | ')[1].split()]}
              for x in data}
for c, v in cards.items():
    cards[c]['my_winning'] = set(v['winning']) & set(v['mine'])
    cards[c]['num_cards'] = 1  # part 2

##a
ans_a = sum([2 ** (len(v['my_winning']) - 1) for v in cards.values() if len(v['my_winning'])])

##b
for c, v in cards.items():
    n_winning = len(v['my_winning'])
    for cp in range(c + 1, c + n_winning + 1):
        if cp in cards:
            cards[cp]['num_cards'] += cards[c]['num_cards']

ans_b = sum([v['num_cards'] for v in cards.values()])

if __name__ == "__main__":
    print(f'Answer {day}a:', ans_a)
    print(f'Answer {day}b:', ans_b)
