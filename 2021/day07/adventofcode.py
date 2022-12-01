import pandas as pd
import numpy as np

with open('day07/adventofcode7.txt', 'r') as f:
    raw = f.readline()
    data = [int(crab) for crab in raw.split(',')]

"""TODAY I INADVERTENTLY HAD PREKNOWLEDGE, KNOWING THAT MEDIAN AND MEAN WERE SOMEHOW A FACTOR, IT ACTUALLY HINDERED
ME MORE THAN IT HELPED ME BUT IT LED TO THE FOLLOWING SOLUTION. SCROLL DOWN FOR MY ATTEMPT AT CODING IT PROPERLY."""
# ## 7a
# # If not median, moving to left or right of middle position costs 1 fuel on 51% of data, therefore suboptimal
# ans_7a = sum([abs(crab - np.median(data)) for crab in data])
#
# ## 7b
# # Fuel burned is 1+2+3+...+n, or as Gauss says n(n+1)/2, or (n^2 + n) / 2 --> basically optimizing the quadratic distance
# # Least squares tells us we optimize quadratic distance by the mean
# dist1 = [abs(crab - np.floor(np.mean(data))) for crab in data]
# dist2 = [abs(crab - np.ceil(np.mean(data))) for crab in data]
# ans_7b = min(sum([(n+1)*n/2 for n in dist1]), sum([(n+1)*n/2 for n in dist2]))

## 7a
minimum = 1e16
for i in range(np.max(data)):
    candidate = sum([abs(crab - i) for crab in data])
    if candidate < minimum:
        minimum = candidate
ans_7a = minimum

## 7b
minimum = 1e16
for i in range(np.max(data)):
    candidate = sum([n*(n+1)/2 for n in [abs(crab - i) for crab in data]])
    if candidate < minimum:
        minimum = candidate
ans_7b = minimum


if __name__ == "__main__":
    print('Answer 7a:', ans_7a)
    print('Answer 7b:', ans_7b)
