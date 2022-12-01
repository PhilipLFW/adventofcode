import numpy as np
np.set_printoptions(linewidth=225)

pw = 51
data = np.pad(np.genfromtxt('day20/adventofcode20.txt', dtype=str, comments='|||',delimiter=1), pw, constant_values='.')

key = '##.....##.#.#####.#...###...#.##..#....##..#.##.#.#....##.....#.##.##.#.#.#...#.#.#.###.##..#.#.#.#..#.##.#...#..#.#.#..#####.##.#..#..##.#..#.#...#.....#.###..#..#####.##...#..##..##...#.#...##.##..##...##.##.#......#...##.##.#####.#....####....######.#.#.......#.############.###..#..#......####......#..##.####.##....#..#.#.###..#.####.####.#.##.##.##..###.#..#.......#....#..########....##..##.#...#.#.###.###.###..#..#.###..#....#.###..#.##.##..###.#.#####....###.##.###.....#######........#.#.##...##.#....'

assert len(key) == 512

def enhance(pixels):
    return key[int(''.join([pixel.replace('.', '0').replace('#', '1') for pixel in pixels.flatten()]),2)]

def print_image(df):
    print(str(df).replace(' [', '').replace('[', '').replace(']', '').replace('\'', '') + '\n')

def enhancement_n(data, n=2):
    data = data.copy()
    print_image(data)
    for i in range(n):
        print(i + 1)
        if i // 2 == i / 2 and key[0] == '#':
            char = '#'
        else:
            char = '.'
        new_data = np.full_like(data, char)
        for x in range(1, data.shape[0] - 1):
            for y in range(1, data.shape[1] - 1):
                new_data[x, y] = enhance(data[(x - 1):(x + 2), (y - 1):(y + 2)])

        data = new_data.copy()
        print_image(data)
    return data

## 20a
ans_20a = sum(sum(enhancement_n(data, 2)=='#'))

## 20b
ans_20b = sum(sum(enhancement_n(data, 50)=='#'))

if __name__ == "__main__":
    print('Answer 20a:', ans_20a)
    print('Answer 20b:', ans_20b)
