import pandas as pd
import numpy as np
from itertools import product
from scipy.sparse import lil_matrix
from copy import deepcopy
from solved import *

with open('day19/adventofcode19.txt', 'r') as f:
    raw = f.readlines()
    data = [txt.replace('\n', '') for txt in raw]


def transform_3d(x, y, z):
    # res = {}
    for i in range(4):
        for j in range(4):
            for k in range(4):
                a = ((i + 1) / 2) * np.pi
                b = ((j + 1) / 2) * np.pi
                c = ((k + 1) / 2) * np.pi
                ## https://pages.mtu.edu/~shene/COURSES/cs3621/NOTES/geometry/geo-tran.html
                rotation_xy = np.array([[int(np.cos(a)), int(-np.sin(a)), 0, 0],
                                        [int(np.sin(a)), int(np.cos(a)), 0, 0],
                                        [0, 0, 1, 0],
                                        [0] * 3 + [1]])
                rotation_yz = np.array([[1, 0, 0, 0],
                                        [0, int(np.cos(b)), int(-np.sin(b)), 0],
                                        [0, int(np.sin(b)), int(np.cos(b)), 0],
                                        [0] * 3 + [1]])
                rotation_xz = np.array([[int(np.cos(c)), 0, int(np.sin(c)), 0],
                                        [0, 1, 0, 0],
                                        [int(-np.sin(c)), 0, int(np.cos(c)), 0],
                                        [0] * 3 + [1]])

                rotation = np.matmul(np.matmul(rotation_xy, rotation_yz), rotation_xz)

                translation = np.array([[x, y, z, 1]])
                # res.add(tuple(np.matmul(rotation, translation.T)[:3, 0]))
                yield tuple(np.matmul(rotation, translation.T)[:3, 0])

def all_transformations(beacon):
    yield from zip(*[transform_3d(*coords) for coords in beacon])

def transform_2d(x, y):
    rotation = np.array([[1, 0],
                         [0, 1],
                         [0] * 2])
    translation = np.array([[x, y, 1]])
    return np.concatenate([rotation, translation.T], axis=1)

raw = """--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14"""
scanners = [txt.split('\n')[1:] for txt in raw.strip().split('\n\n')]

def delta(xyz1, xyz2):
    xyz1, xyz2 = eval(str(xyz1)), eval(str(xyz2))
    return tuple(abs(first-second) for first,second in zip(xyz1, xyz2))

def distance(xyz1, xyz2, return_delta=False):
    dxyz = delta(xyz1, xyz2)
    if return_delta:
        return np.sqrt(sum([d ** 2 for d in dxyz])), min(dxyz), max(dxyz)
    else:
        return np.sqrt(sum([d ** 2 for d in dxyz]))

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
        for rotation_id, rotation in enumerate(orients(beacons)):
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
                break
explore('scanner 0')
## 19a
ans_19a = len(set(sum([list(v) for v in full_map['beacons'].values()], [])))

## 19b
ans_19b = 0

# map = {}
# for i, scanner in enumerate(scanners):
#     max_x, min_x = max([eval(beacon)[0] for beacon in scanner]), min([eval(beacon)[0] for beacon in scanner])
#     max_y, min_y = max([eval(beacon)[1] for beacon in scanner]), min([eval(beacon)[1] for beacon in scanner])
#     dims = max_x - min_x + 1, max_y - min_y + 1
#     map[f'scanner {i}'] = set()
#     for beacon in scanner:
#         x, y = np.array(eval(beacon)) - np.array((min_x, min_y))
#         map[f'scanner {i}'].add((x,y))

scanners = list(map(parse, raw.split("\n\n")))

mapped, diffs = full_match(scanners)
beacons = set()

for view in mapped:
    for point in view:
        beacons.add(point)

print("p1:", len(beacons))


if __name__ == "__main__":
    print('Answer 19a:', ans_19a)
    print('Answer 19b:', ans_19b)
