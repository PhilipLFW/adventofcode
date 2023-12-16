import pandas as pd
import numpy as np
import os
import re

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('/')[-2]
with open(file, 'r') as f:
    data = [txt.replace('\n', '') for txt in f.readlines()]

##a
ans_a = sum([int(list(re.sub('[a-z]', '', x))[0] + list(re.sub('[a-z]', '', x))[-1]) for x in data])


file = 'test2.txt' if TESTING else 'input.txt'
day = os.getcwd().split('/')[-2]
with open(file, 'r') as f:
    data = [txt.replace('\n', '') for txt in f.readlines()]

##b
digits = {'one': '1',
          'two': '2',
          'three': '3',
          'four': '4',
          'five': '5',
          'six': '6',
          'seven': '7',
          'eight': '8',
          'nine': '9',
          '1': '1',
          '2': '2',
          '3': '3',
          '4': '4',
          '5': '5',
          '6': '6',
          '7': '7',
          '8': '8',
          '9': '9'}
pattern = re.compile('|'.join([k for k in digits]))
first = [(k[0]) for k in [[digits[z] for z in re.findall(pattern, x)] for x in data]]

rev_digits = {'eno': '1',
              'owt': '2',
              'eerht': '3',
              'ruof': '4',
              'evif': '5',
              'xis': '6',
              'neves': '7',
              'thgie': '8',
              'enin': '9',
              '1': '1',
              '2': '2',
              '3': '3',
              '4': '4',
              '5': '5',
              '6': '6',
              '7': '7',
              '8': '8',
              '9': '9'}
pattern = re.compile('|'.join([k for k in rev_digits]))
last = [(k[0]) for k in [[rev_digits[z] for z in re.findall(pattern, x[::-1])] for x in data]]

ans_b = sum([int(i + j) for i, j in zip(first, last)])


if __name__ == "__main__":
    print(f'Answer {day[-2]}a:', ans_a)
    print(f'Answer {day[-2]}b:', ans_b)
