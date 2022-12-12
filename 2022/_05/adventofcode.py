import pandas as pd
import numpy as np
import os

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('/')[-1]
with open(file, 'r') as f:
    data = [txt.replace('\n', '') for txt in f.readlines()]

boxes = data[:data.index('')-1]
bases = data[data.index('')-1]
locs = {x: bases.index(x) for x in bases if x != ' '}
instructions = data[data.index('')+1:]
init_stacks = {k: ''.join([box[v] if len(box) >= v else '' for box in boxes]).strip()[::-1] for k, v in locs.items()}

##a
stacks = init_stacks.copy()
for instr in instructions:
    _move, _from, _to = instr.replace('move ', '').replace('from ', '').replace('to ', '').split()
    for _ in range(int(_move)):
        stacks[_to] += stacks[_from][-1]
        stacks[_from] = stacks[_from][:-1]
ans_a = ''.join([x[-1] for x in stacks.values()])

##b
stacks = init_stacks.copy()
for instr in instructions:
    _move, _from, _to = instr.replace('move ', '').replace('from ', '').replace('to ', '').split()
    stacks[_to] += stacks[_from][-int(_move):]
    stacks[_from] = stacks[_from][:-int(_move)]
ans_b = ''.join([x[-1] for x in stacks.values()])

if __name__ == "__main__":
    print(f'Answer {day[-1]}a:', ans_a)
    print(f'Answer {day[-1]}b:', ans_b)
