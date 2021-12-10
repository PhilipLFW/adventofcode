import numpy as np

with open('day10/adventofcode10.txt', 'r') as f:
    raw = f.readlines()
    input = [txt.replace('\n', '') for txt in raw]

## 10a
penalties = {
    ')': 3, ## part 1
    ']': 57,
    '}': 1197,
    '>': 25137,
    '(': 1, ## part 2
    '[': 2,
    '{': 3,
    '<': 4,
}

opening = '([{<'
closing = ')]}>'
illegal = ''
scores = []  # part 2
for row in input:  # row = '[{[{({}]{}}([{[{{{}}([]'
    print(row)
    opened = ''
    for char in row:
        last_opening = opened[-1:]
        looking_for = closing[opening.find(last_opening)]
        if char in opening:
            opened += char
        if char in closing:
            if char==looking_for:
                opened = opened[:-1]
            else:
                print(f'Expected {looking_for}, but found {char} instead.')
                illegal += char
                break
    else:  # part 2 activated if loop not corrupted
        score = 0
        for char in opened[::-1]:
            score = score * 5 + penalties[char]
        print('Score:', score)
        scores += [score]

ans_10a = sum([penalties[char] for char in illegal])

## 10b
ans_10b = int(np.median(scores))

if __name__ == "__main__":
    print('Answer 10a:', ans_10a)
    print('Answer 10b:', ans_10b)
