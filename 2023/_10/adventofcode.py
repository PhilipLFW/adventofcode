import pandas as pd
import numpy as np
import os
# from scipy.sparse import csr_matrix, lil_matrix
# from scipy.sparse.csgraph import shortest_path
np.set_printoptions(threshold=10000, linewidth=225)

TESTING = False

file = 'test5.txt' if TESTING else 'input.txt'
day = os.getcwd().split('_')[-2]
data = np.genfromtxt(file, delimiter=1, dtype=str)
data = np.pad(data, 1, 'constant', constant_values='.')

start = np.argwhere(data == 'S')[0]

# determine shape of start
valid_neighbors = {
    (0, -1): ['-', 'L', 'F'],  # valid left neighbors
    (0, 1):  ['-', '7', 'J'],  # valid right neighbors
    (-1, 0): ['|', '7', 'F'],  # valid up neighbors
    (1, 0): ['|', 'L', 'J'],  # valid down neighbors
}

valid_move = {
    '-': [(0, -1), (0, 1)],  # move left or right
    'J': [(0, -1), (-1, 0)],  # move left or up
    '7': [(0, -1), (1, 0)],  # move left or down
    'L': [(0, 1), (-1, 0)],  # move right or up
    'F': [(0, 1), (1, 0)],  # move right or down
    '|': [(-1, 0), (1, 0)]  # move up or down
}


def get_start_tile(start):
    left, right, up, down = np.array([0, -1]), np.array([0, 1]), np.array([-1, 0]), np.array([1, 0])
    neighbors = [data[tuple(x)] for x in [start + left, start + right, start + up, start + down]]
    match [x in list(valid_neighbors.values())[i] for i, x in enumerate(neighbors)]:
        case [True, True, False, False]:
            start_tile = '-'  # valid left and right
        case [True, False, True, False]:
            start_tile = 'J'  # valid left and up
        case [True, False, False, True]:
            start_tile = '7'  # valid left and down
        case [False, True, True, False]:
            start_tile = 'L'  # valid right and up
        case [False, True, False, True]:
            start_tile = 'F'  # valid right and down
        case [False, False, True, True]:
            start_tile = '|'  # valid up and down
    return start_tile


def get_cycle(data, start):
    start_tile = get_start_tile(start)
    curr_tile = start_tile
    curr = start
    step = 0
    move = tuple(np.array((0,0)) - valid_move[curr_tile][1])  # pretend we came from the other side of the start
    cycle = []
    while curr_tile != 'S':
        cycle += [tuple(curr.copy())]
        move = [x for x in valid_move[curr_tile] if x != tuple(np.array((0, 0)) - move)][0]
        curr += move
        curr_tile = data[tuple(curr)]
        step += 1

    return step, cycle


##a
step, cycle = get_cycle(data, start)
ans_a = step // 2

##b
def print_image(df):
    # for testing
    print(str(df).replace(' [', '').replace('[', '').replace(']', '').replace('\'', '') + '\n')

res = np.empty_like(data)
start_tile = get_start_tile(start)
borders = {  # how many times we pass the edges of the cycle
    '|': 1,  # single line,
    'FJ': 1,  # low-high
    'F7': 2,  # low-low
    'LJ': 2,  # high-high
    'L7': 1  # high-low
}

score = 0
for i in range(data.shape[0]):
    open = False
    section = ''
    for j in range(data.shape[1]):
        if (i, j) in cycle:
            section += data[i, j].replace('S', start_tile)
            # once we stop going horizontally, we can check how many times we open and close the cycle
            if section.replace('-', '') in borders:
                for _ in range(borders[section.replace('-', '')]):
                    open = not open
                section = ''
            res[i, j] = data[i, j]  # print_image for debugging
        elif open:
            res[i, j] = 'I'  # print_image for debugging
            score += 1
        else:
            res[i, j] = 'O'  # print_image for debugging

ans_b = score

if __name__ == "__main__":
    print(f'Answer {day}a:', ans_a)
    print(f'Answer {day}b:', ans_b)
