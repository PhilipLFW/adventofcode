import pandas as pd
import numpy as np
import os

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('_')[-2]
with open(file, 'r') as f:
    data = [txt.replace('\n', '') for txt in f.readlines()]
with open('blocks.txt', 'r') as f:
    blocks = [txt.replace('\n', '') for txt in f.readlines()]

jets = data[0]

def print_image(df):
    # for testing
    print(str(df).replace(' [', '').replace('[', '').replace(']', '').replace('\'', '') + '\n')


newlines = [i for i, x in enumerate(blocks) if x == ''] + [len(blocks)]
grids = []
curr = 0
for i in newlines:
    grids += [np.array([np.array(list(g)) for g in blocks[curr:i]])]
    curr = i + 1

jet_effect = {
    '>': (0, -1),
    '<': (0, 1)
}


def tower_height(n_blocks=2022):
    tower = set([(0, x) for x in range(7)])
    heights = {}
    i = 0
    for _ in range(n_blocks):
        start_point = (max(tower)[0] + 4, 0)
        block = np.argwhere(np.rot90(grids[_ % len(grids)], 2) == '#') + start_point
        while True:
            direction = jets[i % len(jets)]
            candidate = [tuple(x) for x in block + jet_effect[direction]]
            if ((direction == '<' and max([y for x,y in candidate]) <= 6) or
                (direction == '>' and min([y for x,y in candidate]) >= 0)) and not any([c in tower for c in candidate]):
                block += jet_effect[direction]
            i += 1
            if any([tuple(x) in tower for x in block + (-1,0)]):
                tower |= {tuple(x) for x in block}
                break
            else:
                block += (-1, 0)
            # new_units = [tuple(x) for x in block]
            # grid = np.full((max(set(new_units) | tower)[0] + 1, 7), '.')
            # for unit in new_units:
            #     grid[unit] = '@'
            # for unit in tower:
            #     grid[unit] = '#'
            # grid[0, :] = '_'
            # print_image(np.rot90(grid, 2))
        heights[_ + 1] = max(tower)[0]
    return heights

##a
heights = tower_height(10000)
ans_a = heights[2022]

##b
h = np.array(list(heights.values()))
for i in range(1, 2000):
    d = np.diff(h[::i])
    if d[-1] == d[-2] == d[-3] == d[-4]:
        cycle_length = i
        cycle_height_diff = d[-1]
        break

ans_b = ((1000000000000 // cycle_length) - 1) * cycle_height_diff + heights[cycle_length + 1000000000000 % cycle_length]

if __name__ == "__main__":
    print(f'Answer {day}a:', ans_a)
    print(f'Answer {day}b:', ans_b)
