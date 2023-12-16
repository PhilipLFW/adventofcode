import numpy as np

with open('day23/adventofcode23.txt', 'r') as f:
    raw = f.readlines()
    data = np.array([list('{:#^13}'.format(txt.replace('\n', ''))) for txt in raw])

spots = {'00': (1,1), '0a': (1,2), 'ab': (1,4), 'bc': (1,6), 'cd': (1,8), 'd1': (1,10), '11': (1,11)}
homes = {'A': [(2,3), (3,3), (4,3), (5,3)],
         'B': [(2,5), (3,5), (4,5), (5,5)],
         'C': [(2,7), (3,7), (4,7), (5,7)],
         'D': [(2,9), (3,9), (4,9), (5,9)]}
pens = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

def _starts(data):
    return {x: list(sorted({tuple((i,j)) for i,j in zip(*np.where(data==x))})) for x in 'ABCD'}

def distance(tup1, tup2):
    (a,b), (c,d) = tup1, tup2
    return abs(b-d) + abs(a-1) + abs(c-1)  # distance through second line

def energy(step, starts):
    amphipod, step = step.split(':')
    start, end = step.split(' > ')

    if len(start) == 1:
        _from = starts[amphipod][int(start)]
    else:
        _from = spots[start]

    if len(end) == 1:
        _to = homes[amphipod][(int(end))]
    else:
        _to = spots[end]

    return distance(_from, _to) * pens[amphipod]


## 23a
## MANUALLY SOLVED
steps = """A:0 > 00
B:0 > 0a
B:1 > ab
C:1 > 1
A:1 > d1
D:1 > 1
B:ab > 1
B:0a > 0
C:0 > 0
D:0 > 0
A:00 > 1
A:d1 > 0""".split('\n')
starts_a = _starts(data)
ans_23a = sum([energy(step, starts_a) for step in steps])

## 23b
## MANUALLY SOLVED
xlines = """#D#C#B#A#
#D#B#A#C#""".split('\n')
data = np.insert(data, 3,np.array([list('{:#^13}'.format(txt.replace('\n', ''))) for txt in xlines]), axis=0)
starts_b = _starts(data)

steps = """A:0 > 00
B:0 > 11
B:1 > d1
A:2 > 0a
B:3 > cd
C:0 > 3
C:2 > 2
B:2 > bc
D:3 > ab
B:bc > 3
B:cd > 2
B:d1 > 1
B:11 > 0
C:1 > 1
A:1 > 11
C:3 > 0
A:3 > d1
D:ab > 3
D:1 > 2
D:2 > 1
D:3 > 0
A:00 > 3
A:0a > 2
A:d1 > 1
A:11 > 0""".split('\n')
ans_23b = sum([energy(step, starts_b) for step in steps])

if __name__ == "__main__":
    print('Answer 23a:', ans_23a)
    print('Answer 23b:', ans_23b)
