import pandas as pd
import numpy as np
import os
from collections import Counter

TESTING = False

file = 'test.txt' if TESTING else 'input.txt'
day = os.getcwd().split('_')[-2]
with open(file, 'r') as f:
    data = [txt.replace('\n', '') for txt in f.readlines()]

cards = [x.split()[0] for x in data]
bids = [int(x.split()[1]) for x in data]


def hand_strength(cards, joker=False):
    # count initial cards in hand
    counter = [Counter(hand) for hand in cards]

    if joker:
        # replace J by most common card (unless most common card is J and J is not the only card)
        # else replace J by second most common card
        counter = [Counter(hand) for hand in
                   [c.replace('J',
                              counts.most_common()[0][0] if not counts.most_common()[0][0] == 'J' or len(counts) == 1
                              else
                              counts.most_common()[1][0])
                    for c, counts in zip(cards, counter)]]

    # convert to str: possible hand strengths 5, 41, 32, 311, 221, 2111, 1111
    strength = [''.join([str(x) for x in sorted(list(counts.values()))[::-1]]) for counts in counter]

    return strength


def play_game(cards, bids, joker=False):
    # determine sort values
    if not joker:
        vals = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
    else:
        vals = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10}

    # define game as a dataframe
    hands = pd.DataFrame({'cards': cards, 'bid': bids})

    # determine hand strengths
    hands['strength'] = hand_strength(cards, joker=joker)

    # determine order of cards by numerical values
    hands['values'] = hands['cards'].apply(lambda c: [vals[x] if x in vals else int(x) for x in c])
    values_order = sorted(hands['values'])
    hands['order'] = hands['values'].apply(lambda x: values_order.index(x))

    # order by hand strength, then by numerical order in case of tiebreakers
    # possible hand strengths 5, 41, 32, 311, 221, 2111, 1111 already follow order of actual strengths
    hands = hands.sort_values(['strength', 'order'], ascending=True).reset_index(drop=True)

    # rank based on order and determine winnings
    hands['rank'] = hands.index + 1
    hands['winnings'] = hands['bid'] * hands['rank']

    return hands['winnings'].sum()


##a
ans_a = play_game(cards, bids, joker=False)

##b
ans_b = play_game(cards, bids, joker=True)


if __name__ == "__main__":
    print(f'Answer {day}a:', ans_a)
    print(f'Answer {day}b:', ans_b)
