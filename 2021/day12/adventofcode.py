import pandas as pd
import numpy as np

with open('day12/adventofcode12.txt', 'r') as f:
    raw = f.readlines()
    paths = [txt.replace('\n', '') for txt in raw]

reverse_paths = ['-'.join(p.split('-')[::-1]) for p in paths]
connections = paths + reverse_paths
starting_paths = [p for p in connections if p.startswith('start')]

def get_paths(paths, connections, max_passes=1):
    for path in paths:
        _from, _to = path.split('-')
        small_cave_count = [_from.count(_) for _ in set(_from.split(',')) if _.islower() and _ not in ['start', 'end']]  # part 2
        if _to == 'end':  # return this path
            yield ','.join(path.split('-'))
        elif _to == 'start':  # can't move to start
            continue
        elif max_passes == 1 and _to.islower() and _to in _from:  # already been in this small cave
            continue
        ## Next to elif statements belong to part 2
        elif small_cave_count and 1 < max_passes < max(small_cave_count):  # one small cave has been visited more than allowed
            continue
        elif small_cave_count and 1 < max_passes <= max(small_cave_count) and _to.islower() and _from.count(_to) >= max_passes - 1:  # this small cave has reached the max visits but another one already reached max visits before
            continue
        else:
            paths_from_to = [','.join(path.split('-')[:-1]) + ',' + p for p in connections if p.startswith(_to)]
            if len(paths_from_to) > 0:
                yield from get_paths(paths_from_to, connections, max_passes)

## 12a
ans_12a = len([i for i in get_paths(starting_paths, connections, max_passes=1)])

## 12b
ans_12b = len([i for i in get_paths(starting_paths, connections, max_passes=2)])

if __name__ == "__main__":
    print('Answer 12a:', ans_12a)
    print('Answer 12b:', ans_12b)