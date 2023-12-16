import pandas as pd
import numpy as np
import os
from collections import defaultdict

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('/')[-1]
with open(file, 'r') as f:
    data = [txt.replace('\n', '') for txt in f.readlines()]

##a
cwd = 'root'
memory = defaultdict(int)
for line in data:
    if line[0] == '$':
        if 'cd' in line:
            if '..' in line:
                cwd = '/'.join(cwd.split('/')[:-2]) + '/'
            else:
                dir = line.split()[-1]
                cwd += dir + '/' if dir != '/' else dir
    else:
        _one, _two = line.split()
        if _one != 'dir':
            for i, _ in enumerate(cwd.split('/')[:-1]):
                dir = '/'.join(cwd.split('/')[:i+1]) + '/'
                memory[dir] += int(_one)

ans_a = sum([x for x in memory.values() if x <= 1e5])

##b
space_used = 7e7 - memory['root/']
space_needed = 3e7 - space_used
ans_b = min([x for x in memory.values() if x >= space_needed])

if __name__ == "__main__":
    print(f'Answer {day[-1]}a:', ans_a)
    print(f'Answer {day[-1]}b:', ans_b)
