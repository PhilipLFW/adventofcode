import pandas as pd
import numpy as np

octo = np.genfromtxt("day11/adventofcode11.txt", delimiter=1, dtype=int)


def flashing_octo_single_step(octo):
    flashed = set()
    add = np.ones_like(octo)
    while sum(sum(add)) >= 1:
        add = np.zeros_like(octo)
        flash = np.where(octo>=9)
        for i, j in zip(*flash):
            if (i,j) not in flashed:
                flashed.add((i, j))
                add[max(i-1, 0):(i+2), max(j-1, 0):(j+2)] += 1
            else:
                continue
        octo += add
    octo += 1
    for i, j in flashed:
        octo[i,j] = 0
    return octo, len(flashed)

## 11a
flashed_octo = 0
octo_a = octo.copy()
for step in range(100):
    octo_a, n_flashed = flashing_octo_single_step(octo_a)
    flashed_octo += n_flashed
    print(f'After step {step + 1} ({flashed_octo} flashed):\n', octo_a)

ans_11a = flashed_octo

## 11b
step = 0
octo_b = octo.copy()
while not np.all(octo_b==0):
    octo_b, _ = flashing_octo_single_step(octo_b)
    step += 1

ans_11b = step

if __name__ == "__main__":
    print('Answer 11a:', ans_11a)
    print('Answer 11b:', ans_11b)
