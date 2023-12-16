import pandas as pd
import numpy as np
import os

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('/')[-1]
with open(file, 'r') as f:
    data = [txt.replace('\n', '') for txt in f.readlines()]

##a
contained = 0
for pairs in data:
    one, two = pairs.split(',')
    lb1, ub1 = one.split('-')
    lb2, ub2 = two.split('-')
    if (int(lb1) <= int(lb2) and int(ub1) >= int(ub2)) or (int(lb2) <= int(lb1) and int(ub2) >= int(ub1)):
        contained += 1
ans_a = contained

##b
overlap = 0
for pairs in data:
    one, two = pairs.split(',')
    lb1, ub1 = one.split('-')
    lb2, ub2 = two.split('-')
    elf1 = range(int(lb1), int(ub1)+1)
    elf2 = range(int(lb2), int(ub2)+1)
    if set(elf1) & set(elf2):
        overlap += 1
ans_b = overlap

if __name__ == "__main__":
    print(f'Answer {day[-1]}a:', ans_a)
    print(f'Answer {day[-1]}b:', ans_b)
