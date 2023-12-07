import pandas as pd
import numpy as np
import os
from collections import Counter

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('_')[-2]
with open(file, 'r') as f:
    data = [txt.replace('\n', '') for txt in f.readlines()]

##a
cards = [x.split()[0] for x in data]
bids = [int(x.split()[1]) for x in data]
vals = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}

def no_joker(cards, bids):
    vals = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
    hands = pd.DataFrame({'cards': cards, 'bid': bids})
    hands['strength'] = [''.join([str(x) for x in sorted(list(Counter(hand).values()))[::-1]]) for hand in cards]
    hands['values'] = hands['cards'].apply(lambda c: [vals[x] if x in vals else int(x) for x in c])
    values_order = sorted(hands['values'])
    hands['order'] = hands['values'].apply(lambda x: values_order.index(x))
    hands = hands.sort_values(['strength', 'order'], ascending=True).reset_index(drop=True)
    hands['rank'] = hands.index + 1
    hands['winnings'] = hands['bid'] * hands['rank']

    return hands

ans_a = no_joker(cards, bids)['winnings'].sum()

##b
def joker(cards, bids):
    vals = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10}
    hands = pd.DataFrame({'cards': cards, 'bid': bids})

    hands['counter'] = [Counter(hand) for hand in cards]
    hands['strength'] = [''.join([str(x) for x in sorted(list(Counter(hand).values()))[::-1]])
                         for hand in [c.replace('J', x.most_common()[1][0] if len(x.most_common()) > 1 and x.most_common()[0][0] == 'J' else x.most_common()[0][0])
                                      for c, x in zip(hands['cards'], hands['counter'])]]
    hands['values'] = hands['cards'].apply(lambda c: [vals[x] if x in vals else int(x) for x in c])
    values_order = sorted(hands['values'])
    hands['order'] = hands['values'].apply(lambda x: values_order.index(x))
    hands = hands.sort_values(['strength', 'order'], ascending=True).reset_index(drop=True)
    hands['rank'] = hands.index + 1
    hands['winnings'] = hands['bid'] * hands['rank']

    return hands

ans_b = joker(cards, bids)['winnings'].sum()

if __name__ == "__main__":
    print(f'Answer {day}a:', ans_a)
    print(f'Answer {day}b:', ans_b)
