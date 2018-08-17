from random import randint
class Solution:

    def __init__(self, n_rows, n_cols):
        self.map = {}
        self.r = n_rows
        self.c = n_cols
        self.end = n_rows * n_cols - 1

    def flip(self):
        ind = randint(0, self.end)
        val = self.map[ind] if ind in self.map else ind
        self.map[ind] = self.end if self.end not in self.map else self.map[self.end]
        self.end -= 1
        return [val // self.c, val % self.c]

    def reset(self):
        self.end = self.r * self.c - 1
        self.map = {}

