import pandas as pd
import numpy as np

with open('day08/adventofcode8.txt', 'r') as f:
    raw = f.readlines()
    data = [txt.replace('\n', '') for txt in raw]

## 8a
total = 0
for display in data:
    input, output = display.split(' | ')
    total += sum([len(x) in [2, 3, 4, 7] for x in output.split(' ')])
ans_8a = total

## 8b
def haschars(string, chars):
    return set(string).intersection(set(chars)) == set(chars)

def get_decoder(input):
    this_in = input.split(' ')
    decoder = {
        1: [''.join(sorted(_)) for _ in this_in if len(_)==2][0],
        4: [''.join(sorted(_)) for _ in this_in if len(_)==4][0],
        7: [''.join(sorted(_)) for _ in this_in if len(_)==3][0],
        8: [''.join(sorted(_)) for _ in this_in if len(_)==7][0],
    }
    helper_14 = ''.join(set(decoder[4]) - set(decoder[1])) # The |_ part of the 4
    decoder.update({
        0: [''.join(sorted(_)) for _ in this_in if len(_)==6 and not haschars(_, helper_14)][0],
        2: [''.join(sorted(_)) for _ in this_in if len(_)==5 and not haschars(_, helper_14) and not haschars(_, decoder[7])][0],
        3: [''.join(sorted(_)) for _ in this_in if len(_)==5 and haschars(_, decoder[1])][0],
        5: [''.join(sorted(_)) for _ in this_in if len(_)==5 and haschars(_, helper_14)][0],
        6: [''.join(sorted(_)) for _ in this_in if len(_)==6 and not haschars(_, decoder[1])][0],
        9: [''.join(sorted(_)) for _ in this_in if len(_)==6 and haschars(_, decoder[4])][0]
    })
    return {v: str(k) for k, v in decoder.items()}

total = 0
for display in data:
    input, output = display.split(' | ')
    decoder = get_decoder(input)
    code = ''.join([decoder[''.join(sorted(_))] for _ in output.split(' ')])
    total += int(code)

ans_8b = total

if __name__ == "__main__":
    print('Answer 8a:', ans_8a)
    print('Answer 8b:', ans_8b)
