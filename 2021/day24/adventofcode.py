import numpy as np
from string import ascii_letters

with open('adventofcode.txt', 'r') as f:
    raw = f.readlines()
    data = [txt.replace('\n', '') for txt in raw]

# text file translated to a.txt
# remove all operations that (are supposed to) do nothing
# what's left is that one of two things happens:
# 1. z multiplied by 26 and w + constant gets added to z
# 2. z divided by 26  (but for this x + constant must match w)


class ALU:
    def __init__(self, input, instructions):
        self.input = input
        self.instructions = instructions
        self.w = 0
        self.x = 0
        self.y = 0
        self.z = 0
        self.ix = 0

        # Import alphabet to represent base 26
        self.alphabet = ascii_letters[26:]
        self.repr_z = ''

        self.run()

    @staticmethod
    def mul(a, b):
        return int(a * b)

    @staticmethod
    def add(a, b):
        return int(a + b)

    @staticmethod
    def mod(a, b):
        return int(a % b)

    @staticmethod
    def div(a, b):
        return int(a / b)

    @staticmethod
    def eql(a, b):
        return int(a == b)

    def inp(self, var):
        setattr(self, var, int(self.input[self.ix]))
        print(f'{self.ix + 1}:', getattr(self, var), self.repr_z)
        self.ix += 1

    def run(self):
        for i, instruction in enumerate(self.instructions):
            if instruction.split(' ')[0] == 'inp':
                var = instruction.split(' ')[1]
                self.inp(var)
            else:
                func, a, b = instruction.split(' ')
                res = getattr(self, func)(getattr(self, a), getattr(self, b) if b in self.__dir__() else int(b))
                setattr(self, a, res)
                # Line 16 of every 18-line chunk of instructions contains the constant added to z with the input
                if i % 18 == 15:
                    self.repr_z += self.alphabet[int(b) + self.w - 1] if self.x else ''
                # Line 5 of every 18-line chunk for 7 of 14 chunks contains a statement that removes last base-26 digit
                if i % 18 == 4 and instruction == 'div z 26':
                    self.repr_z = self.repr_z[:-1]


## 24a
i = 69914999975369 + 1  # number derived from setting to 99999999999999 and trying to follow instructions in a.txt
                        # with as high of a number as possible
while i > 1e13:
    i -= 1
    res = ALU(str(i), data)
    if res.z == 0:
        break
ans_24a = i

## 24b
i = 14911675311114 - 1  # number derived from setting to 11111111111111 and trying to follow instructions in a.txt
                        # with as low of a number as possible
while i < 1e14:
    i += 1
    res = ALU(str(i), data)
    if res.z == 0:
        break
ans_24b = i

if __name__ == "__main__":
    print('Answer 24a:', ans_24a)
    print('Answer 24b:', ans_24b)
