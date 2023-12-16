import pandas as pd
import numpy as np

with open('day14/adventofcode14.txt', 'r') as f:
    raw = f.readlines()
    polymer = 'SHPPPVOFPBFCHHBKBNCV'
    insertions = [txt.replace('\n', '') for txt in raw]
insertion_dict = {ins.split(' -> ')[0]: ins.split(' -> ')[1] for ins in insertions}

## 14a
fused = polymer
for step in range(10):
    print('Step:', step + 1)
    orig = fused
    fused = fused[0]
    for pairs in zip(orig[:-1], orig[1:]):
        pair = ''.join(pairs)
        if pair in insertion_dict:
            fused += insertion_dict[pair] + pairs[1]
char_count = [fused.count(_) for _ in set(fused)]
ans_14a = max(char_count) - min(char_count)

## 14b
pair_counts = {k: 0 for k in insertion_dict.keys()}
for pairs in zip(polymer[:-1], polymer[1:]):
    pair = ''.join(pairs)
    if pair in insertion_dict:
        pair_counts[pair] += 1
new_pairs = {k: [k[0]+v, v+k[1]] for k,v in insertion_dict.items()}

for step in range(40):
    keep = pair_counts.copy()
    pair_counts = {k: 0 for k in keep.keys()}
    for k, v in keep.items():
        if keep[k] >= 1:
            for p in new_pairs[k]:
                if p in keep:
                    pair_counts[p] += v
unique_chars = set(''.join(insertion_dict.keys()))
res = []
for _ in unique_chars:
    res += [sum([int(k.find(_)==0) * v for k, v in pair_counts.items()]) + (1 if _ == polymer[-1] else 0)]
ans_14b = max(res) - min(res)

if __name__ == "__main__":
    print('Answer 14a:', ans_14a)
    print('Answer 14b:', ans_14b)
