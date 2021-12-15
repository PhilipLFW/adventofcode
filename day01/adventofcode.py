import pandas as pd
##1a
data = pd.read_csv('day01/adventofcode.csv', header=None)
ans_1a = (data - data.shift()>0).sum()

##1b
new = (data + data.shift(-1) + data.shift(-2))
ans_1b = (new-new.shift()>0).sum()

if __name__ == "__main__":
    print('Answer 1a:', ans_1a)
    print('Answer 1b:', ans_1b)