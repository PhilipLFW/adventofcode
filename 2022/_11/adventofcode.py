import pandas as pd
import numpy as np
import os

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('/')[-2]
with open(file, 'r') as f:
    data = [txt.replace('\n', '') for txt in f.readlines()]

monkeys = [x for x, _ in enumerate(data) if 'Monkey' in x]
starting_items = [[int(j) for j in x.split(': ')[1].split(', ')] for x in data if 'Starting items' in x]
operation = [x.split('new = ')[1] for x in data if 'Operation' in x]
test = ['i' + x.split(':')[1].replace('divisible by', '%') for x in data if 'Test' in x]
yes = [x.split('throw to ')[1].capitalize() for x in data if 'true' in x]
no = [x.split('throw to ')[1].capitalize() for x in data if 'false' in x]

starting_items = {k: v for k, v in zip(monkeys, starting_items)}
operation = {k: v for k, v in zip(monkeys, operation)}
test = {k: v for k, v in zip(monkeys, test)}
yes = {k: v for k, v in zip(monkeys, yes)}
no = {k: v for k, v in zip(monkeys, no)}
inspected = {k: 0 for k in monkeys}

##a
for round in range(20):
    for monkey, items in starting_items.items():
        inspected[monkey] += len(items)
        while items:
            old = items[0]
            starting_items[monkey][0] = eval(operation[monkey]) // 3
            i = starting_items[monkey].pop(0)
            if not eval(test[monkey]):
                starting_items[yes[monkey]] += [i]
            else:
                starting_items[no[monkey]] += [i]

ans_a = np.prod(sorted(list(inspected.values()))[-2:])

monkeys = [x[:-1] for x in data if 'Monkey' in x]
starting_items = [[int(j) for j in x.split(': ')[1].split(', ')] for x in data if 'Starting items' in x]
operation = [x.split('new = ')[1] for x in data if 'Operation' in x]
test = ['i' + x.split(':')[1].replace('divisible by', '%') for x in data if 'Test' in x]
yes = [x.split('throw to ')[1].capitalize() for x in data if 'true' in x]
no = [x.split('throw to ')[1].capitalize() for x in data if 'false' in x]

starting_items = {k: v for k, v in zip(monkeys, starting_items)}
operation = {k: v for k, v in zip(monkeys, operation)}
test = {k: v for k, v in zip(monkeys, test)}
yes = {k: v for k, v in zip(monkeys, yes)}
no = {k: v for k, v in zip(monkeys, no)}
inspected = {k: 0 for k in monkeys}

##b
shared_factor = np.prod([int(x.split(' % ')[1]) for x in test.values()])
for round in range(10000):
    for monkey, items in starting_items.items():
        inspected[monkey] += len(items)
        while items:
            old = items[0]
            starting_items[monkey][0] = eval(operation[monkey]) % shared_factor
            i = starting_items[monkey].pop(0)
            if not eval(test[monkey]):
                starting_items[yes[monkey]] += [i]
            else:
                starting_items[no[monkey]] += [i]

ans_b = np.prod(sorted(list(inspected.values()))[-2:])

if __name__ == "__main__":
    print(f'Answer {day[-2]}a:', ans_a)
    print(f'Answer {day[-2]}b:', ans_b)
