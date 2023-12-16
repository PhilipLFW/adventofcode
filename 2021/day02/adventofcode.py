import pandas as pd
##2a
df = pd.read_csv('day02/adventofcode2.csv', header=None)
position = [0, 0]
for i, row in df.iterrows():
    instr, pos = row[0].split(' ')
    if instr == 'forward':
        position[0] += int(pos)
    if instr == 'up':
        position[1] -= int(pos)
    if instr == 'down':
        position[1] += int(pos)
ans_2a = (position[0] * position[1])

##2b
position = [0, 0, 0]
for i, row in df.iterrows():
    instr, pos = row[0].split(' ')
    if instr == 'forward':
        position[0] += int(pos)
        position[1] += int(pos) * position[2]
    if instr == 'up':
        position[2] -= int(pos)
    if instr == 'down':
        position[2] += int(pos)
ans_2b = (position[0] * position[1])

if __name__ == "__main__":
    print('Answer 2a:', ans_2a)
    print('Answer 2b:', ans_2b)