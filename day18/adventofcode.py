import numpy as np
from copy import deepcopy

with open('day18/adventofcode18.txt', 'r') as f:
    raw = f.readlines()
    fish = [eval(txt.replace('\n', '')) for txt in raw]

class Snailfish:
    def __init__(self, fish):
        self.fish = deepcopy(fish)
        self._init_helpers()
        self.reduce()

    def _init_helpers(self):
        self.carry_left = 0
        self.carry_right = 0
        self.level_1 = []
        self.level_2 = []
        self.level_3 = []
        self.level_4 = []
        self.positions = []
        self.to_explode = []
        self.to_split = []
        self.selected = False
        self.keep_going = False

    def _set_levels(self, fish, level=1, index=None):
        index = [0] if index is None or level == 1 else index
        for i, x in enumerate(fish):
            index[-1] = i
            if type(x) != list:
                self.positions += [index.copy()]
                setattr(self, 'level_' + str(level), getattr(self, 'level_' + str(level)) + [x])
            else:
                if level < 4:
                    self._set_levels(x, level + 1, index=index + [i])
                else:
                    self.level_4 += [x]
                    if not self.selected:
                        self.to_explode = index.copy()
                        self.positions += [self.to_explode]
                        # self.positions += [index + [0]] + [index + [1]]
                        self.selected = True
                    else:
                        self.positions += [index + [0]] + [index + [1]]

    def _get_levels(self):
        for level in range(4):
            print(f'Level {level + 1}:', getattr(self, 'level_' + str(level + 1)))

    def get_position(self, index):
        ix = len(index)
        if ix == 1:
            return self.fish[index[0]]
        if ix == 2:
            return self.fish[index[0]][index[1]]
        if ix == 3:
            return self.fish[index[0]][index[1]][index[2]]
        if ix == 4:
            return self.fish[index[0]][index[1]][index[2]][index[3]]
        if ix == 5:
            return self.fish[index[0]][index[1]][index[2]][index[3]][index[4]]

    def get_left_of(self, index):
        index = index if index in self.positions else index + [0]
        pos = self.positions.index(index)
        if pos > 0:
            return self.get_position(self.positions[pos - 1])

    def get_right_of(self, index):
        index = index if index in self.positions else index + [1]
        pos = self.positions.index(index)
        if pos < len(self.positions):
            return self.get_position(self.positions[self.positions.index(index) + 1])

    def set_position(self, index, val):
        ix = len(index)
        if ix == 1:
            self.fish[index[0]] = val
        if ix == 2:
            self.fish[index[0]][index[1]] = val
        if ix == 3:
            self.fish[index[0]][index[1]][index[2]] = val
        if ix == 4:
            self.fish[index[0]][index[1]][index[2]][index[3]] = val
        if ix == 5:
            self.fish[index[0]][index[1]][index[2]][index[3]][index[4]] = val

    def increase(self, index, val):
        val = val + self.get_position(index)
        self.set_position(index, val)

    def increase_left(self, index):
        index = index if index in self.positions else index + [0]
        pos = self.positions.index(index)
        if pos > 0:
            self.increase(self.positions[pos - 1], self.carry_left)

    def increase_right(self, index):
        index = index if index in self.positions else index + [1]
        pos = self.positions.index(index)
        if pos + 1 < len(self.positions):
            self.increase(self.positions[self.positions.index(index) + 1], self.carry_right)

    def explode(self):
        self.carry_left, self.carry_right = self.get_position(self.to_explode)
        self.increase_left(self.to_explode)
        self.increase_right(self.to_explode)
        self.set_position(self.to_explode, 0)

    def split(self):
        val = self.get_position(self.to_split)
        self.set_position(self.to_split, [int(val//2), int(np.ceil(val/2))])

    def add(self, fish):
        self.fish = [self.fish] + [fish]

    def reduce(self):
        self._init_helpers()
        self._set_levels(self.fish)
        self.to_split = [pos for pos in self.positions if type(self.get_position(pos)) != list and self.get_position(pos) > 9]
        if self.to_explode:
            self.explode()
            self.keep_going = True
        elif self.to_split:
            self.to_split = self.to_split[0]
            self.split()
            self.keep_going = True
        if self.keep_going:
            self.reduce()

    def add_fish(self, fish):
        self.add(fish)
        self.reduce()

    def magnitude_left(self, left):
        if type(left) != list:
            return left
        else:
            return self.magnitude(left)

    def magnitude_right(self, right):
        if type(right) != list:
            return right
        else:
            return self.magnitude(right)

    def magnitude(self, pair=None):
        left, right = pair if pair else self.fish
        return 3 * self.magnitude_left(left) + 2 * self.magnitude_right(right)


fish_a = deepcopy(fish)
snailfish_hw = Snailfish(fish_a[0].copy())
for f in fish_a[1:]:
    snailfish_hw.add_fish(f)

## 18a
ans_18a = snailfish_hw.magnitude()

fish_b = deepcopy(fish)
max_magnitude = 0
for f in fish_b.copy():
    for other in [fsh for fsh in fish_b if fsh != f].copy():
        print(f, other)
        snailfish_hw = Snailfish(deepcopy(f))
        snailfish_hw.add_fish(deepcopy(other))
        this_magnitude = snailfish_hw.magnitude()
        if this_magnitude < max_magnitude:
            print(f'MAGNITUDE: {this_magnitude} < {max_magnitude}')
        else:
            print(f'MAGNITUDE: {this_magnitude} >= {max_magnitude}')
        max_magnitude = max(max_magnitude, this_magnitude)

## 18b
ans_18b = max_magnitude

if __name__ == "__main__":
    print('Answer 18a:', ans_18a)
    print('Answer 18b:', ans_18b)
