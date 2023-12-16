import pandas as pd

##3a
df = pd.read_csv('day03/adventofcode3.txt', header=None, dtype=str)

digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for ix, row in df.iterrows():
    for i, j in enumerate(row[0]):
        digits[i] += int(j)

gamma = digits.copy()
epsilon = digits.copy()
for k, l in enumerate(gamma):
    if l > len(df) / 2:
        gamma[k] = 1
        epsilon[k] = 0
    else:
        gamma[k] = 0
        epsilon[k] = 1

gmm = int(''.join([str(i) for i in gamma]), 2)
eps = int(''.join([str(i) for i in epsilon]), 2)

ans_3a = gmm * eps

##3b
ox = df[0].copy().to_list()
co2 = df[0].copy().to_list()
digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 0
while len(ox) > 1:
    for row in ox:
        digits[i] += int(row[i])
    if digits[i] >= len(ox) / 2:
        print('yes')
        ox = [rows for rows in ox if rows[i] == '1']
        print(ox)
    else:
        print('no')
        ox = [rows for rows in ox if rows[i] == '0']
        print(ox)
    i += 1

digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 0
while len(co2) > 1:
    for row in co2:
        digits[i] += int(row[i])
    if digits[i] < len(co2) / 2:
        print('yes')
        co2 = [rows for rows in co2 if rows[i] == '1']
        print(co2)
    else:
        print('no')
        co2 = [rows for rows in co2 if rows[i] == '0']
        print(co2)
    i += 1

o2 = int(''.join([str(i) for i in ox]), 2)
co = int(''.join([str(i) for i in co2]), 2)

ans_3b = o2 * co

if __name__ == "__main__":
    print('Answer 3a:', ans_3a)
    print('Answer 3b:', ans_3b)