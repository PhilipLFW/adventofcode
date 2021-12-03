import pandas as pd
##1a
data = pd.read_csv('adventofcode.csv', header=None)
ans_1a = (data - data.shift()>0).sum()

##1b
new = (data + data.shift(-1) + data.shift(-2))
ans_1b = (new-new.shift()>0).sum()