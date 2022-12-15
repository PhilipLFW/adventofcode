import os

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('/')[-2]
with open(file, 'r') as f:
    data = [txt.replace('\n', '') for txt in f.readlines()]

sensors = [eval(x.split(': ')[0].replace('Sensor at ', '').replace('x=', '').replace(' y=', '')) for x in data]
beacons = [eval(x.split(': ')[1].replace('closest beacon is at ', '').replace('x=', '').replace(' y=', '')) for x in data]
distances = [abs(sx - bx) + abs(sy - by) for (sx, sy), (bx, by) in zip(sensors, beacons)]

##a
no_beacon = set()
target_y = 10 if TESTING else 2000000
for sensor, beacon, manhattan in zip(sensors, beacons, distances):
    sx, sy = sensor
    bx, by = beacon
    vdist = abs(sy-target_y)
    if vdist > manhattan:
        continue
    else:
        no_beacon |= {(sx - manhattan + dx, target_y) for dx in range(abs(manhattan - vdist) * 2 + 1)} - {beacon}
ans_a = len(no_beacon)

##b
space = 20 if TESTING else 4000000
candidates = {(0, 0), (0, space), (space, 0), (space, space)}
for i, ((sx, sy), dist) in enumerate(zip(sensors, distances)):
    print(i + 1, len(sensors))
    # beacon can not be more than 1 outside of a sensors range, otherwise 1 step closer would be a candidate solution
    # draw lines on the outside of the range where there can be no beacon (i.e. dist + 1)
    dist += 1
    top = (sx - dist, sy)
    bottom = (sx + dist, sy)
    left = (sx, sy - dist)
    right = (sx, sy + dist)
    lines = (top, right), (right, bottom), (bottom, left), (left, top)
    for line in lines:
        for x, y in zip(range(line[0][0], line[1][0]), range(line[0][1], line[1][1])):
            if 0 <= x < space and 0 <= y < space:
                candidates |= {(x, y)}

for i, (cx, cy) in enumerate(candidates.copy()):
    if not i % 200000:
        print(i, len(candidates))
    for (sx, sy), dist in zip(sensors, distances):
        this_dist = abs(cx - sx) + abs(cy - sy)
        if this_dist <= dist:
            candidates -= {(cx, cy)}

res = list(candidates)[0] if len(candidates) == 1 else 'ERROR'
ans_b = res[0] * 4000000 + res[1]

if __name__ == "__main__":
    print(f'Answer {day[-2]}a:', ans_a)
    print(f'Answer {day[-2]}b:', ans_b)
