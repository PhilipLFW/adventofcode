import numpy as np

data = np.genfromtxt('adventofcode25.txt', dtype=str, comments='|||', delimiter=1)


def print_image(df):
    """use for testing"""
    print(str(df).replace(' [', '').replace('[', '').replace(']', '').replace('\'', '') + '\n')

## 25a
south, east = data.shape

i = 0
old = np.ones_like(data)
new = data.copy()
print_image(new)
while not np.all(old == new):
    i += 1
    old = new.copy()
    for y in list(range(east))[::-1]:
        for x in range(south):
            if old[x, y] == '>' and old[x, (y + 1) % east] == '.':
                new[x, (y + 1) % east] = '>'
                new[x, y] = '.'
    mid = new.copy()
    for x in list(range(south))[::-1]:
        for y in range(east):
            if mid[x, y] == 'v' and mid[(x + 1) % south, y] == '.':
                new[(x + 1) % south, y] = 'v'
                new[x, y] = '.'

ans_25a = i

## 25b
ans_25b = None

if __name__ == "__main__":
    print('Answer 25a:', ans_25a)
    print('Answer 25b:', ans_25b)
