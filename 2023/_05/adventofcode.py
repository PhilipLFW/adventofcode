import pandas as pd
import numpy as np
import os
from collections import defaultdict

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('_')[-2]
with open(file, 'r') as f:
    data = [txt.replace('\n', '') for txt in f.readlines()]

seeds = [int(x) for x in data[0].split(': ')[1].split()]
soil_map = data[data.index('seed-to-soil map:')+1:data.index('soil-to-fertilizer map:')-1]
fertilizer_map = data[data.index('soil-to-fertilizer map:')+1:data.index('fertilizer-to-water map:')-1]
water_map = data[data.index('fertilizer-to-water map:')+1:data.index('water-to-light map:')-1]
light_map = data[data.index('water-to-light map:')+1:data.index('light-to-temperature map:')-1]
temperature_map = data[data.index('light-to-temperature map:')+1:data.index('temperature-to-humidity map:')-1]
humidity_map = data[data.index('temperature-to-humidity map:')+1:data.index('humidity-to-location map:')-1]
location_map = data[data.index('humidity-to-location map:')+1:]

def map_to_dict(seed, mapper):
    for m in mapper:
        dest, src, n = [int(x) for x in m.split()]
        if src <= seed < src + n:
            seed = seed + (dest - src)
            break
    return seed

def seeds_to_locs(seeds):
    locs = []
    for i, seed in enumerate(seeds):
        seed = map_to_dict(seed, soil_map)
        seed = map_to_dict(seed, fertilizer_map)
        seed = map_to_dict(seed, water_map)
        seed = map_to_dict(seed, light_map)
        seed = map_to_dict(seed, temperature_map)
        seed = map_to_dict(seed, humidity_map)
        seed = map_to_dict(seed, location_map)
        locs += [seed]
    return locs


##a
ans_a = min(seeds_to_locs(seeds))

##b
# working out example manually
# seed_ranges = [(79, 93), (55, 68)]
# soil_ranges = [(98, 99), (50, 97)] # [(79, 93), (55, 68)] ->  # [(81, 95), (57, 70)]
# fertilizer_ranges = [(15, 51), (52, 53), (0, 14)] # [(81, 95), (57, 70)]
# water_ranges = [(53, 60), (11, 52), (0, 6), (7, 10)] # [(81, 95), (57, 60), (61, 70)] -> # [(81, 95), (53, 56), (61, 70)]
# light_ranges = [(18, 24), (25, 94)] # [(53, 56), (61, 70), (81, 94), (94, 95)] -> # [(46, 49), (54, 63), (74, 87), (95, 95)]
# temperature_ranges = [(77, 99), (45, 63), (64, 76)] # [(46, 49), (54, 63), (74, 76), (77, 87), (95, 95)] -> # [(82, 85), (90, 99), (78, 80), (45, 55), (63, 63)]
# humidity_ranges = [(69, 69), (0, 68)] # [(82, 85), (90, 99), (78, 80), (45, 55), (63, 63)] -> [(82, 85), (90, 99), (78, 80), (46, 56), (64, 64)]
# location_ranges = [(56, 92), (93, 96)] # [(82, 85), (90, 92), (93, 96), (97, 99), (78, 80), (46, 55), (56, 56), (64, 64)] -> [(86, 89), (94, 96), (56, 59), (97, 99), (82, 84), (46, 55), (60, 60), (68, 68)]

new_seeds = [(seeds[s * 2], seeds[s * 2] + seeds[s * 2 + 1]) for s in range(len(seeds) // 2)]

def get_borders(seeds, mapper):
    # init empty list for mapping result
    new_seeds = []

    # check all source-destination combos and sort them from lowest to highest
    mappers = []
    for m in mapper:
        dest, src, n = [int(x) for x in m.split()]
        shift = dest - src
        left, right = (src, src + n - 1)
        mappers += [(left, right, shift)]
    mappers = sorted(mappers)
    mappers.insert(0, (0, mappers[0][0], 0))
    mappers.append((mappers[-1][1] + 1, np.Inf, 0))

    for pair in seeds:
        all_ranges = [(max(x[0], y[0]) + y[2], min(x[1], y[1] - 1) + y[2]) for x, y in zip([pair] * len(mappers), mappers) if y[1] != 0]
        new_seeds += [x for x in all_ranges if x[1] >= x[0]]

    return sorted(new_seeds)

new_seeds = get_borders(new_seeds, soil_map)
new_seeds = get_borders(new_seeds, fertilizer_map)
new_seeds = get_borders(new_seeds, water_map)
new_seeds = get_borders(new_seeds, light_map)
new_seeds = get_borders(new_seeds, temperature_map)
new_seeds = get_borders(new_seeds, humidity_map)
new_seeds = get_borders(new_seeds, location_map)


ans_b = new_seeds[0][0]

if __name__ == "__main__":
    print(f'Answer {day}a:', ans_a)
    print(f'Answer {day}b:', ans_b)
