import pandas as pd
import numpy as np
import os

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('/')[-1]
with open(file, 'r') as f:
    data = [txt.replace('\n', '') for txt in f.readlines()][0]

##a
for i in range(len(data)):
    marker = data[i:i+4]
    if len(set(marker)) == 4:
        break

ans_a = i + 4

##b
for i in range(len(data)):
    marker = data[i:i+14]
    if len(set(marker)) == 14:
        break

ans_b = i + 14

if __name__ == "__main__":
    print(f'Answer {day[-1]}a:', ans_a)
    print(f'Answer {day[-1]}b:', ans_b)
