import pandas as pd
import os

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('/')[-1]
with open(file, 'r') as f:
    data = [int(txt.replace('\n', '')) if txt != '\n' else '' for txt in f.readlines()]

##a
calories = data.copy()
chunks = []
while calories:
    blank = calories.index('') if '' in calories else 100
    chunks += [sum(calories[:blank])]
    calories = calories[blank + 1:]
ans_a = max(chunks)

##b
ans_b = sum(sorted(chunks, reverse=True)[:3])

if __name__ == "__main__":
    print(f'Answer {day[-1]}a:', ans_a)
    print(f'Answer {day[-1]}b:', ans_b)
