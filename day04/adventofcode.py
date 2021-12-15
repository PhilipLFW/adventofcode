import numpy as np

with open('day04/adventofcode4.txt', 'r') as f:
    raw = f.readlines()
    text = sum([[int(nmbrs) for nmbrs in txt.replace('\n', '').split()] for txt in raw if txt != '\n'], [])
bingo_cards_rows = np.reshape(text, (100,5,5)).tolist()
bingo_cards_columns = np.swapaxes(bingo_cards_rows, 1, 2).tolist()
bingo_cards = [row + col for row, col in zip(bingo_cards_rows, bingo_cards_columns)]
bingo_numbers = [62,55,98,93,48,28,82,78,19,96,31,42,76,25,34,4,18,80,66,6,
                 14,17,57,54,90,27,40,47,9,36,97,56,87,61,91,1,64,71,99,38,
                 70,5,94,85,49,59,69,26,21,60,0,79,2,95,11,84,20,24,8,51,
                 46,44,88,22,16,53,7,32,89,67,15,86,41,92,10,77,68,63,43,75,
                 33,30,81,37,83,3,39,65,12,45,23,73,72,29,52,58,35,50,13,74]

##4a
ix = 0
while all([len([x for x in card if x != []]) >= 10 for card in bingo_cards]):
    next = bingo_numbers[ix]
    print(f'No bingo..., the next number is {next}')
    for p, card in enumerate(bingo_cards):
        bingo_cards[p] = [[nmbr for nmbr in rowcol if nmbr != next] for rowcol in card]
    ix += 1
winning_card = np.where([len([x for x in card if x != []]) < 10 for card in bingo_cards])[0][0]
print(f'BINGO! The winner is: {winning_card + 1}')
ans_4a = sum(sum(bingo_cards[winning_card][:5], [])) * next


##4b
ix = 0
remaining_players = set(range(1, 101))
while len(bingo_cards) > 1:
    next = bingo_numbers[ix]
    if any([len([x for x in card if x != []]) < 10 for card in bingo_cards]):
        winning_cards = np.where([len([x for x in card if x != []]) < 10 for card in bingo_cards])[0]
        remaining_players = remaining_players - set([list(remaining_players)[i] for i in winning_cards])
        print(f'BINGO! Numbers: {", ".join([str(winner) for winner in winning_cards + 1])}, '
              f'Remaining players: {len(remaining_players)}, '
              f'the next number is {next}')
        bingo_cards = [card for card in bingo_cards if len([x for x in card if x != []]) >= 10]
    else:
        print(f'No bingo..., the next number is {next}')
    for p, card in enumerate(bingo_cards):
        bingo_cards[p] = [[nmbr for nmbr in rowcol if nmbr != next] for rowcol in card]
    ix += 1
print(f'The BIG loser is: {remaining_players}')
ans_4b = sum(sum(bingo_cards[0][:5], [])) * next

if __name__ == "__main__":
    print('Answer 4a:', ans_4a)
    print('Answer 4b:', ans_4b)
