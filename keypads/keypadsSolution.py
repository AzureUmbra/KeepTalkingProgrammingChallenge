from random import randint, sample
from keypadsTest import keypadsTest


class keypadsSolution:
    def __init__(self):
        self.symbols = [[1, 2, 3, 4, 5, 6, 7], [8, 1, 7, 9, 10, 6, 11], [12, 13, 9, 14, 15, 3, 10],
                   [16, 17, 18, 5, 14, 11, 19], [20, 19, 18, 21, 17, 22, 23], [16, 8, 24, 25, 20, 26, 27]]

    def generate(self):
        self.selection = self.symbols[randint(0,len(self.symbols)-1)]
        self.pad = sample(self.selection,4)

        self.solution = []
        for i in self.selection:
            if i in self.pad:
                self.solution.append(self.pad.index(i))
        return self.pad

    def solve(self,guess):
        if guess == self.solution:
            return True
        else:
            return False


if __name__ == '__main__':
    s = keypadsSolution()
    keypadsTest(s,25)