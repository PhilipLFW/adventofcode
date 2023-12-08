import pandas as pd
import numpy as np
import os
from collections import defaultdict
from math import lcm

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('_')[-2]
with open(file, 'r') as f:
    data = [txt.replace('\n', '') for txt in f.readlines()]

instr = data[0].replace('R', '1').replace('L', '0')
nodes = {x.split(' = ')[0]: x.split(' = ')[1].replace('(', '').replace(')', '').split(', ') for x in data[2:]}

##a
def walk(instr):
    instr = instr.replace('R', '1').replace('L', '0')

    curr = 'AAA'
    step = 0
    while curr != 'ZZZ':
        curr = nodes[curr][int(instr[step % len(instr)])]
        step += 1
    return step

ans_a = walk(instr)


file = 'test2.txt' if TESTING else 'input.txt'
day = os.getcwd().split('_')[-2]
with open(file, 'r') as f:
    data = [txt.replace('\n', '') for txt in f.readlines()]

instr = data[0].replace('R', '1').replace('L', '0')
nodes = {x.split(' = ')[0]: x.split(' = ')[1].replace('(', '').replace(')', '').split(', ') for x in data[2:]}


##b
def walk_simul(instr):
    instr = instr.replace('R', '1').replace('L', '0')
    start = [node for node in nodes if node.endswith('A')]
    cycle_z = defaultdict(list)
    curr = start.copy()
    step = 0
    while not all([len(cycle_z[c]) >= 2 for c in start]):
        curr = [nodes[c][int(instr[step % len(instr)])] for c in curr]
        zs = [node.endswith('Z') for node in curr]
        if any(zs):
            for node in np.array(start)[zs]:
                cycle_z[node] += [step]
        step += 1

    common_step = lcm(*[np.diff(cycle_z[x])[0] for x in start])

    return common_step


ans_b = walk_simul(instr)

if __name__ == "__main__":
    print(f'Answer {day}a:', ans_a)
    print(f'Answer {day}b:', ans_b)
