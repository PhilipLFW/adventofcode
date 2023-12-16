import pandas as pd
import numpy as np

with open('day17/adventofcode17.txt', 'r') as f:
    raw = f.readline().split(': ')[1].split(', ')

# raw = """target area: x=20..30, y=-10..-5""".split(': ')[1].split(', ')
x_min, x_max = [int(val) for val in raw[0].replace('x=','').split('..')]
y_min, y_max = [int(val) for val in raw[1].replace('y=','').split('..')]

def trajectory(init_velo: tuple):
    velo = np.array(init_velo)
    pos = np.array([0,0])
    highest_y = 0
    # print('Position:', pos, 'Velocity:', velo)
    while not (x_min <= pos[0] <= x_max and y_min <= pos[1] <= y_max):
        if sum([pos[0] > x_max and velo[0] > 0, pos[0] < x_max and velo[0] < 0, pos[1] <= y_min]):
            return set(), 0
        pos += velo
        highest_y = max(highest_y, pos[1])
        velo[0] -= np.sign(velo[0])
        velo[1] -= 1
        # print('Position:', pos, 'Velocity:', velo)
    else:
        return {init_velo}, highest_y

# {n: n*(n+1)/2 for n in range(100)}  # check the minimum x
all_success = set()
highest = 0
for x in range(15,200):
    for y in range(-100, 100):
        success, highest_y = trajectory((x,y))
        highest = max(highest, highest_y)
        all_success = all_success.union(success)

## 17a
ans_17a = highest

## 17b
ans_17b = len(all_success)

if __name__ == "__main__":
    print('Answer 17a:', ans_17a)
    print('Answer 17b:', ans_17b)
