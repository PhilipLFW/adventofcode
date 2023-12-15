import pandas as pd
import numpy as np
import os
from scipy.sparse import csr_matrix, lil_matrix
from scipy.sparse.csgraph import shortest_path
from functools import cache

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('/')[-2]
with open(file, 'r') as f:
    data = [txt.replace('\n', '') for txt in f.readlines()]

valves = [x.split()[1] for x in data]
flows = [int(x.split()[4].replace('rate=', '').replace(';', '')) for x in data]
paths = {v: ''.join(x.split(';')[1].split()[4:]).split(',') for v, x in zip(valves, data)}
positive = [v for f, v in zip(flows, valves) if f > 0]


def get_distance_graph():
    dists = lil_matrix((len(valves), len(valves)))
    for v, ps in paths.items():
        for p in ps:
            dists[valves.index(v), valves.index(p)] += 1
    return csr_matrix(dists)

graph = get_distance_graph()
dists, pre = shortest_path(graph, directed=True, return_predecessors=True)

# open = []
# closed = np.array([1 for _ in valves])
# path = []
# pressure = 0
# total = 0
# position = 'AA'
# minutes = 30
# while minutes:
#     print(f'== Minute {30 - minutes + 1} ==')
#     if len(open) > 1:
#         print(f'Valves {", ".join(open[:-1])} and {open[-1]} are open, releasing {pressure} pressure.')
#         total += pressure
#     elif len(open) == 1:
#         print(f'Valve {open[0]} is open, releasing {pressure} pressure.')
#         total += pressure
#     else:
#         print('No valves are open.')
#     path += [position]
#
#     posix = valves.index(position)
#     walk_places(minutes, posix, np.array(flows), closed, pressure=0)
#     gains = (np.array(flows) * (minutes - (dists[posix] + 1))) * closed # 1 extra for opening the valve
#     # gains = np.array(flows) / (dists[posix] + 1)  # 1 extra for opening the valve
#
#     for ix in np.where(gains > 0)[0]:
#         gains = (np.array(flows) * (minutes - (dists[ix] + 1)))  # 1 extra for opening the valve
#         gains[ix] = 0
#         # gains = np.array(flows) / (dists[posix] + 1)  # 1 extra for opening the valve
#         gains[[not x for x in closed]] = 0
#
#     move = np.argmax(gains)
#     next = move
#     for _ in range(int(dists[posix, move]) - 1):
#         next = pre[posix, next]
#
#     if next == posix and flows[posix]:
#         print(f'You open valve {position}.')
#         open += [position]
#         closed[posix] = False
#         pressure += flows[posix]
#     elif next != posix:
#         print(f'You move to valve {valves[next]}.')
#         position = valves[next]
#     minutes -= 1
#
# ## a
# ans_a = total

@cache
def walk_places(minutes, posix=valves.index('AA'), closed=frozenset(positive), elephant=False):
    mins_remaining = (minutes - (dists[posix] + 1))
    gains = (flows * mins_remaining)
    gains[[x not in closed for x in valves]] = 0
    gains[posix] = 0
    options = list(np.where(mins_remaining > 1)[0])
    walk = [gains[ix] + walk_places(mins_remaining[ix], ix, closed - {valves[ix]}, elephant)
            for ix in options]
    walk_elephant = walk_places(26, closed=closed) if elephant else 0
    return max(walk + [walk_elephant])

flows = np.array(flows)
## a
ans_a = walk_places(30)

## b
ans_b = walk_places(26, elephant=True)


if __name__ == "__main__":
    print(f'Answer {day[-2]}a:', ans_a)
    print(f'Answer {day[-2]}b:', ans_b)
