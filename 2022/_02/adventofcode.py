import pandas as pd
import os

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('/')[-1]
with open(file, 'r') as f:
    data = [txt.replace('\n', '') for txt in f.readlines()]

outcomes = {
    'A Y': 8,  # ROCK PAPER = W (6) + 2
    'B Z': 9,  # PAPER SCISSORS = W (6) + 3
    'C X': 7,  # SCISSORS ROCK = W (6) + 1
    'A Z': 3,  # ROCK SCISSORS = L (0) + 3
    'B X': 1,  # PAPER ROCK = L (0) + 1
    'C Y': 2,  # SCISSORS PAPER = L (0) + 2
    'A X': 4,  # ROCK ROCK = D (3) + 1
    'B Y': 5,  # PAPER PAPER = D (3) + 2
    'C Z': 6   # SCISSORS SCISSORS = D (3) + 3
}

##a
ans_a = sum([outcomes[game] for game in data])


outcomes = {
    'A X': 3,  # ROCK LOSE = SCISSORS (3) + 0
    'A Y': 4,  # ROCK DRAW = ROCK (1) + 3
    'A Z': 8,  # ROCK WIN = PAPER (2) + 6
    'B X': 1,  # PAPER LOSE = ROCK (1) + 0
    'B Y': 5,  # PAPER DRAW = PAPER (2) + 3
    'B Z': 9,  # PAPER WIN = SCISSORS (3) + 6
    'C X': 2,  # SCISSORS LOSE = PAPER (2) + 0
    'C Y': 6,  # SCISSORS DRAW = SCISSORS (3) + 3
    'C Z': 7   # SCISSORS WIN = ROCK (1) + 6
}

##b
ans_b = sum([outcomes[game] for game in data])

if __name__ == "__main__":
    print(f'Answer {day[-1]}a:', ans_a)
    print(f'Answer {day[-1]}b:', ans_b)
