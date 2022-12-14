import numpy as np
import os
np.set_printoptions('threshold', 10000)
TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('/')[-2]
with open(file, 'r') as f:
    data = [txt.replace('\n', '') for txt in f.readlines()]


def print_image(df):
    """use for testing"""
    print(str(df).replace(' [', '').replace('[', '').replace(']', '').replace('\n  ', ' ').replace('\'', '') + '\n')


def setup_cave(data, left=None, right=None, add_depth=0, add_floor=False, show_image=True):
    left = left if left else min([min([int(k.split(',')[0]) for k in j]) for j in [i.split(' -> ') for i in data]])
    right = right if right else max([max([int(k.split(',')[0]) for k in j]) for j in [i.split(' -> ') for i in data]])
    depth = max([max([int(k.split(',')[1]) for k in j]) for j in [i.split(' -> ') for i in data]]) + 1 + add_depth
    cave = np.full_like(np.zeros((depth, right - left + 1)), '.', dtype=str)
    cave[0, 500 - left] = '+'

    for path in data:
        nodes = path.split(' -> ')
        prev_node = None
        for node in nodes:
            y, x = [int(z) for z in node.split(',')]
            y -= left
            if prev_node:
                prev_y, prev_x = [int(z) for z in prev_node.split(',')]
                prev_y -= left
                cave[min(prev_x, x):(max(prev_x, x) + 1), min(prev_y, y):(max(prev_y, y) + 1)] = '#'
            prev_node = node

    if add_floor:
        cave[-1, :] = '#'
    if show_image:
        print_image(cave)
    return cave


def falling_sand(cave, show_image=True):
    res = None
    i = 0
    sand_source = tuple(np.array(np.where(cave == '+')).flatten())
    while not res:
        _x, _y = sand_source
        for _ in range(cave.shape[0]):
            try:
                if cave[_x + 1, _y] == '.':
                    _x += 1
                elif cave[_x + 1, _y - 1] == '.':
                    _x += 1
                    _y -= 1
                elif cave[_x + 1, _y + 1] == '.':
                    _x += 1
                    _y += 1
                else:
                    if cave[_x, _y] != 'o':
                        cave[_x, _y] = 'o'
                    else:
                        res = i
                    break
            except IndexError:
                res = i
                break
        i += 1
    if show_image:
        print_image(cave)
    return res


##a
# cave
cave = setup_cave(data)
ans_a = falling_sand(cave)

##b
cave = setup_cave(data, 0, 1000, 2, True, False)
ans_b = falling_sand(cave, False)

if __name__ == "__main__":
    print(f'Answer {day[-2]}a:', ans_a)
    print(f'Answer {day[-2]}b:', ans_b)
