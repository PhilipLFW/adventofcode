import pandas as pd
import numpy as np
from itertools import product,permutations
from copy import deepcopy

def die():
    for i in list(range(1,101)) * 1000:
        yield i


def play(p1, p2):
    p1 = [p1, 0]
    p2 = [p2, 0]
    i = 0
    a = die()
    while p1[1] < 1000 and p2[1] < 1000:
        roll = next(a) + next(a) + next(a)
        if i // 2 == i / 2:
            p1 = step(*p1, roll)
        else:
            p2 = step(*p2, roll)
        i += 1

    return i * 3, min(p1[1], p2[1])


def step(pos, score, roll):
    return (pos + roll - 1) % 10 + 1, score + (pos + roll - 1) % 10 + 1

def turn(state, player, turns, goal=21):
    new = {}
    winning = 0
    for game, n in state.items():
        (pos1, score1), (pos2, score2) = game
        for k, v in turns.items():
            if player == 1:
                new_pos, new_score = step(pos1, score1, k)
                new_game = ((new_pos, new_score), (pos2, score2))
            else:
                new_pos, new_score = step(pos2, score2, k)
                new_game = ((pos1, score1), (new_pos, new_score))
            if new_score < goal:
                try:
                    current = new[new_game]
                except KeyError:
                    current = 0
                new[new_game] = current + n * v
            else:
                winning += n * v
    return new, winning

def quantum_play(p1, p2, **kwargs):
    a = [a[0] + a[1] + a[2] for a in list(product([1,2,3], [1,2,3], [1,2,3]))]
    turns = {i: a.count(i) for i in set(a)}

    p = {((p1,0), (p2,0)): 1}
    p1_wins = 0
    p2_wins = 0

    while p:
        p, wins = turn(p, 1, turns, **kwargs)
        p1_wins += wins

        p, wins = turn(p, 2, turns, **kwargs)
        p2_wins += wins

    return p1_wins, p2_wins

## 21a
ans_21a = np.product(play(10, 9))

## 21b
ans_21b = max(quantum_play(10, 9))

if __name__ == "__main__":
    print('Answer 21a:', ans_21a)
    print('Answer 21b:', ans_21b)
