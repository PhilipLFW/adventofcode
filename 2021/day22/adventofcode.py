import pandas as pd
import numpy as np
import re

with open('day22/adventofcode22.txt', 'r') as f:
    raw = f.readlines()
    data = [txt.replace('\n', '') for txt in raw]

instructions = [eval(re.sub('(on|off) x=(.+)\\.\\.(.+),y=(.+)\\.\\.(.+),z=(.+)\\.\\.(.+)',
                    '"\\1", (\\2, \\3), (\\4, \\5), (\\6, \\7)',line)) for line in data]

x = [-50, 51]
y = [-50, 51]
z = [-50, 51]
for instr, (x1, x2), (y1, y2), (z1, z2) in instructions:
    x += [x1, x2+1]
    y += [y1, y2+1]
    z += [z1, z2+1]

def orders(a):
    return {v: k for k,v in enumerate(sorted(set(a)))}

def volumes(a):
    return {k: v for k,v in enumerate(np.ediff1d(sorted(set(a))))}

ox, vx = orders(x), volumes(x)
oy, vy = orders(y), volumes(y)
oz, vz = orders(z), volumes(z)


def switch_a(lower=-50, upper=50):
    dim = upper - lower + 1
    cubes = np.zeros((dim, dim, dim))
    for instr, (x1,x2), (y1, y2), (z1,z2) in instructions:
        x1, x2 = max(x1, lower) - lower, min(x2, upper) - lower + 1
        y1, y2 = max(y1, lower) - lower, min(y2, upper) - lower + 1
        z1, z2 = max(z1, lower) - lower, min(z2, upper) - lower + 1
        if instr == 'on':
            cubes[x1:x2, y1:y2, z1:z2] = 1
        else:
            cubes[x1:x2, y1:y2, z1:z2] = 0
    return cubes
## 22a
cubes = switch_a()
ans_22a = np.sum(cubes)

## 22b
def switch_b():
    dims = len(ox)+1, len(oy)+1, len(oz)+1
    cubes = np.zeros(dims)
    for instr, (x1,x2), (y1, y2), (z1,z2) in instructions:
        x1, x2 = ox[x1], ox[x2+1]
        y1, y2 = oy[y1], oy[y2+1]
        z1, z2 = oz[z1], oz[z2+1]
        if instr == 'on':
            cubes[x1:x2, y1:y2, z1:z2] = 1
        else:
            cubes[x1:x2, y1:y2, z1:z2] = 0
    res = 0
    for x,y,z in zip(*np.nonzero(cubes)):
        res += vx[x]*vy[y]*vz[z]
    return res
ans_22b = switch_b()

if __name__ == "__main__":
    print('Answer 22a:', ans_22a)
    print('Answer 22b:', ans_22b)
