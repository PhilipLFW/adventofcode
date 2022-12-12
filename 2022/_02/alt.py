import pandas as pd
import os

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('/')[-1]
with open(file, 'r') as f:
    data = [txt.replace('\n', '') for txt in f.readlines()]


player_1 = 'ABC'
player_2 = 'XYZ'


##a
score = 0
for game in data:
    p1, p2 = game.split(' ')
    rps_1 = player_1.index(p1)
    rps_2 = player_2.index(p2)
    # first part gets winner (-2 wins, -1 loses, 0 ties, +1 wins, +2 loses)
    # second part gets player 2's choice (+1 to get the score)
    score += ((rps_2 - rps_1 + 4) % 3) * 3 + rps_2 + 1

ans_a = score


##b
score = 0
for game in data:
    p1, p2 = game.split(' ')
    rps_1 = player_1.index(p1)
    rps_2 = player_2.index(p2)
    # first part gets winner (X=0, Y=1*3, Z=2*3)
    # second part gets player 2's choice (+2 to lose, +1 to win, 0 to tie, +1 to get score)
    score += rps_2 * 3 + (rps_1 + (rps_2 + 2) % 3) % 3 + 1
ans_b = score

if __name__ == "__main__":
    print(f'Answer {day[-1]}a:', ans_a)
    print(f'Answer {day[-1]}b:', ans_b)
