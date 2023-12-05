import pandas as pd
import numpy as np
import os
from collections import defaultdict

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('_')[-2]
with open(file, 'r') as f:
    data = [txt.replace('\n', '') for txt in f.readlines()]

seeds = pd.Series([x for x in data[0].split(': ')[1].split()])
soil_map = data[data.index('seed-to-soil map:')+1:data.index('soil-to-fertilizer map:')-1]
fertilizer_map = data[data.index('soil-to-fertilizer map:')+1:data.index('fertilizer-to-water map:')-1]
water_map = data[data.index('fertilizer-to-water map:')+1:data.index('water-to-light map:')-1]
light_map = data[data.index('water-to-light map:')+1:data.index('light-to-temperature map:')-1]
temperature_map = data[data.index('light-to-temperature map:')+1:data.index('temperature-to-humidity map:')-1]
humidity_map = data[data.index('temperature-to-humidity map:')+1:data.index('humidity-to-location map:')-1]
location_map = data[data.index('humidity-to-location map:')+1:]

def map_to_dict(_map):
    res = {}
    for m in _map:
        dest, src, n = [int(x) for x in m.split()]
        for s, d in zip(range(src, src + n), range(dest, dest + n)):
            res[str(s)] = str(d)
    return res

soil_map = map_to_dict(soil_map)
fertilizer_map = map_to_dict(fertilizer_map)
water_map = map_to_dict(water_map)
light_map = map_to_dict(light_map)
temperature_map = map_to_dict(temperature_map)
humidity_map = map_to_dict(humidity_map)
location_map = map_to_dict(location_map)


##a
ans_a = (seeds.replace(soil_map).replace(fertilizer_map).replace(water_map).replace(light_map)
         .replace(temperature_map).replace(humidity_map).replace(location_map).astype(int).min())

##b
ans_b = None

if __name__ == "__main__":
    print(f'Answer {day}a:', ans_a)
    print(f'Answer {day}b:', ans_b)
