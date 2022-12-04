import pandas as pd
import numpy as np
from string import ascii_letters as letters
import os

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('/')[-1]
with open(file, 'r') as f:
    data = [txt.replace('\n', '') for txt in f.readlines()]

##a
common = []
for rucksack in data:
    first = rucksack[:len(rucksack)//2]
    second = rucksack[len(rucksack)//2:]
    common += list(set(first) & set(second))
ans_a = sum([letters.index(x) + 1 for x in common])

##b
common = []
for group in range(len(data)//3):
    first, second, third = data[group*3:(group+1)*3]
    common += list(set(first) & set(second) & set(third))

ans_b = sum([letters.index(x) + 1 for x in common])

if __name__ == "__main__":
    print(f'Answer {day[-1]}a:', ans_a)
    print(f'Answer {day[-1]}b:', ans_b)
