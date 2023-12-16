import numpy as np

with open('day05/adventofcode5.txt', 'r') as f:
    raw = f.readlines()
    lines = [txt.replace('\n', '').split(' -> ') for txt in raw]

## 5a
grid = np.zeros([1000, 1000])
for start, end in lines:
    x1,y1 = eval(start)
    x2,y2 = eval(end)

    if x1 == x2:
        ys = np.linspace(y1, y2, num=abs(y2-y1)+1).astype(int)
        grid[ys, x1] += 1
    if y1 == y2:
        xs = np.linspace(x1, x2, num=abs(x2-x1)+1).astype(int)
        grid[y1, xs] += 1

ans_5a = len(grid[grid>1])

## 5b
grid = np.zeros([1000, 1000])
for start, end in lines:
    x1,y1 = eval(start)
    x2,y2 = eval(end)

    xs = np.linspace(x1, x2, num=abs(x2 - x1) + 1).astype(int)
    ys = np.linspace(y1, y2, num=abs(y2 - y1) + 1).astype(int)

    if x1 == x2:
        grid[ys, x1] += 1
    elif y1 == y2:
        grid[y1, xs] += 1
    elif abs(x2-x1) == abs(y2-y1):
        for x,y in zip(xs, ys):
            grid[y, x] += 1
    else:
        continue

ans_5b = len(grid[grid>1])

if __name__ == "__main__":
    print('Answer 5a:', ans_5a)
    print('Answer 5b:', ans_5b)
