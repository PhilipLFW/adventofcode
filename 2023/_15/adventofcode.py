import pandas as pd
import numpy as np
import os
from collections import defaultdict, OrderedDict

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('_')[-2]
with open(file, 'r') as f:
    data = [txt.replace('\n', '').split(',') for txt in f.readlines()][0]

score = 0
for x in data:
    hash_score = 0
    for char in x:
        hash_score += ord(char)
        hash_score *= 17
        hash_score %= 256
    score += hash_score

##a
ans_a = score

##b
boxes = defaultdict(OrderedDict)
for x in data:
    if '=' in x:
        label, focal_length = x.split('=')
        operation = '='
    else:
        label = x[:-1]
        operation = '-'
    box = 0
    for char in label:
        box += ord(char)
        box *= 17
        box %= 256
    if operation == '=':
        boxes[box][label] = int(focal_length)
    else:
        boxes[box].pop(label, None)

score = 0
for box, contents in boxes.items():
    for i, (label, focal_length) in enumerate(contents.items()):
        score += (box + 1) * (i + 1) * focal_length

ans_b = score

if __name__ == "__main__":
    print(f'Answer {day}a:', ans_a)
    print(f'Answer {day}b:', ans_b)
