import pandas as pd
import numpy as np
from functools import lru_cache

with open('day19/adventofcode19.txt', 'r') as f:
    raw = f.read()
    scanners = [txt.split('\n')[1:] for txt in raw.split('\n\n')]


@lru_cache
def rotation_xy(a):
    return np.array([[int(np.cos(a)), int(-np.sin(a)), 0, 0],
                     [int(np.sin(a)), int(np.cos(a)) , 0, 0],
                     [0             , 0              , 1, 0],
                     [0             , 0              , 0, 1]])

@lru_cache
def rotation_yz(b):
    return np.array([[1, 0,              0,               0],
                     [0, int(np.cos(b)), int(-np.sin(b)), 0],
                     [0, int(np.sin(b)), int(np.cos(b)) , 0],
                     [0, 0,              0,               1]])

@lru_cache
def rotation_xz(c):
    return np.array([[int(np.cos(c)) , 0, int(np.sin(c)), 0],
                     [0              , 1, 0             , 0],
                     [int(-np.sin(c)), 0, int(np.cos(c)), 0],
                     [0              , 0, 0             , 1]])

def transform_3d(x, y, z):
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if (j > 0 and k > 0) or j==2:
                    continue
                a = (i / 2) * np.pi
                b = (j / 2) * np.pi
                c = (k / 2) * np.pi
                rotation = np.matmul(np.matmul(rotation_xy(c), rotation_yz(b)), rotation_xz(a))

                translation = np.array([[x, y, z, 1]])
                yield tuple(np.matmul(rotation, translation.T)[:3, 0])

def all_transformations(beacon):
    yield from zip(*[transform_3d(*coords) for coords in beacon])

def transform_2d(x, y):
    rotation = np.array([[1, 0],
                         [0, 1],
                         [0] * 2])
    translation = np.array([[x, y, 1]])
    return np.concatenate([rotation, translation.T], axis=1)

def delta(xyz1, xyz2):
    xyz1, xyz2 = eval(str(xyz1)), eval(str(xyz2))
    return tuple(abs(first-second) for first,second in zip(xyz1, xyz2))

def edist(dxyz):
    return np.sqrt(sum([d ** 2 for d in dxyz]))

def mdist(dxyz):
    return sum([d for d in dxyz])

def distance(xyz1, xyz2, return_delta=False, method=edist):
    dxyz = delta(xyz1, xyz2)
    if return_delta:
        return method(dxyz), min(dxyz), max(dxyz)
    else:
        return method(dxyz)

def diff_tup(xyz1, xyz2):
    xyz1, xyz2 = eval(str(xyz1)), eval(str(xyz2))
    return tuple(x1 - x2 for x1, x2 in zip(xyz1, xyz2))

def offset_tup(xyz1, xyz2):
    xyz1, xyz2 = eval(str(xyz1)), eval(str(xyz2))
    return tuple(x1 + x2 for x1, x2 in zip(xyz1, xyz2))


original = {'scanner 0': {eval(scan) for scan in scanners[0]}}
for i, scanner in enumerate(scanners):
    original[f'scanner {i}'] = set()
    for beacon in scanner:
        x, y, z = np.array(eval(beacon)) # - np.array((min_x, min_y, min_z))
        original[f'scanner {i}'].add(tuple((x,y,z)))

full_map = {'scanners': {'scanner 0': (0,0,0)}, 'beacons': {'scanner 0': original['scanner 0']}, 'explored': set()}
def explore(scan_from):
    print('EXPLORING:', scan_from)
    for scan_to, beacons in original.items():  # scan, beacons = list(map.items())[1]
        if tuple((scan_to, scan_from)) in full_map['explored'] or scan_to==scan_from:
            continue
        full_map['explored'].add(tuple((scan_to, scan_from)))
        full_map['explored'].add(tuple((scan_from, scan_to)))
        print('TRYING:', scan_to)
        for rotation_id, rotation in enumerate(all_transformations(beacons)):
            distances = {}
            for coords in rotation:
                for beacon in full_map['beacons'][scan_from]:
                    distances[str(beacon) + '<->' + str(coords)] = \
                        str(tuple(round(x,4) for x in distance(coords, beacon, return_delta=True))) + ',' + str(rotation_id)
            distances = pd.DataFrame.from_dict(distances, orient='index')
            distances['N'] = distances[0].map(distances[0].value_counts().to_dict())
            distances['rotation'] = [x.split(',')[-1] for x in distances[0]]
            if max(distances['N']) >= 12:
                distances = distances.loc[distances['N']==distances['N'].max()].copy()
                distances.loc[:, ['from', 'to']] = distances.index.str.split('<->').to_list()
                orientation = list(set([diff_tup(x, y) for x, y in zip(distances['from'],distances['to'])]))[0]
                full_map['scanners'][scan_to] = orientation
                print(distances, orientation)
                full_map['beacons'][scan_to] = set()
                for coords in rotation:
                    full_map['beacons'][scan_to].add(offset_tup(coords, full_map['scanners'][scan_to]))
                explore(scan_to)
                print('CONTINUE:', scan_from)
                break

## 19a
explore('scanner 0')
ans_19a = len(set(sum([list(v) for v in full_map['beacons'].values()], [])))

## 19b
max_dist = 0
for i, x1 in full_map['scanners'].items():
    for j, x2 in full_map['scanners'].items():
        dist = distance(x1, x2, method=mdist)
        if dist > max_dist:
            print('New Maximum:', i, j, dist)
            max_dist = max(max_dist, distance(x1, x2, method=mdist))
ans_19b = max_dist

if __name__ == "__main__":
    print('Answer 19a:', ans_19a)
    print('Answer 19b:', ans_19b)
