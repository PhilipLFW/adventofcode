import pandas as pd
import numpy as np
import os

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('_')[-2]
data = np.genfromtxt(file, delimiter=1, dtype=str, comments=None)

def reset_directional_data():
    return {str(d): data.copy() for d in '<>^v'}

def print_image(df):
    # for testing
    print(str(df).replace(' [', '').replace('[', '').replace(']', '').replace('\'', '').replace('\\\\','\\') + '\n')

def print_res(e):
    res = data.copy()
    for x,y in e:
        res[x, y] = '#'
    print_image(res)

def beam(x=0, y=0, d='>'):
    """
    Recursive function calculating the trajectory of the beam
    :param x: the x position at which the beam starts
    :param y: the y position at which the beam starts
    :param d: the direction of the beam, either <, >, ^, or v
    :return: the trajectory of the beam without changing direction
    """
    assert d in '<>^v'

    energized = set()
    try:
        if d in '<>':
            for j in range(y, data.shape[1] if d == '>' else 0 - 1, 1 if d == '>' else -1):
                energized |= {(x, j)}
                match directional_data[d][x, j], d:
                    case '.' , _:
                        directional_data[d][x, j] = d  # use such that we can identify if we've been there before
                        continue
                    case '-', _:
                        continue
                    case '\\', '>':
                        energized |= beam(x + 1, j, 'v')
                        break
                    case '\\', '<':
                        energized |= beam(x - 1, j, '^')
                        break
                    case '/', '>':
                        energized |= beam(x - 1, j, '^')
                        break
                    case '/', '<':
                        energized |= beam(x + 1, j, 'v')
                        break
                    case '|', _:
                        energized |= beam(x + 1, j, 'v')
                        energized |= beam(x - 1, j, '^')
                        break
                    case d, _:
                        break  # no need to stay on the path if we've been there before
        else:
            for i in range(x, data.shape[0] if d == 'v' else 0 - 1, 1 if d == 'v' else -1):
                energized |= {(i, y)}
                match directional_data[d][i, y], d:
                    case '.', _:
                        directional_data[d][i, y] = d
                        continue
                    case '|', _:
                        continue
                    case '\\', 'v':
                        energized |= beam(i, y + 1, '>')
                        break
                    case '\\', '^':
                        energized |= beam(i, y - 1, '<')
                        break
                    case '/', 'v':
                        energized |= beam(i, y - 1, '<')
                        break
                    case '/', '^':
                        energized |= beam(i, y + 1, '>')
                        break
                    case '-', _:
                        energized |= beam(i, y + 1, '>')
                        energized |= beam(i, y - 1, '<')
                        break
                    case d, _:
                        break
    except RecursionError:
        # except when it gets stuck in an infinite loop
        pass

    # print_res(energized)
    return energized

##a
directional_data = reset_directional_data()
ans_a = len(beam())

##b
scores = []
for i in range(data.shape[0]):
    directional_data = reset_directional_data()
    scores.append(len(beam(i, 0, '>')))
for i in range(data.shape[0]):
    directional_data = reset_directional_data()
    scores.append(len(beam(i, data.shape[1] - 1, '<')))
for j in range(data.shape[1]):
    directional_data = reset_directional_data()
    scores.append(len(beam(0, j, 'v')))
for j in range(data.shape[1]):
    directional_data = reset_directional_data()
    scores.append(len(beam(data.shape[0] - 1, j, '^')))

ans_b = max(scores)

if __name__ == "__main__":
    print(f'Answer {day}a:', ans_a)
    print(f'Answer {day}b:', ans_b)
