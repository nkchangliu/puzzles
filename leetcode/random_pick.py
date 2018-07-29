from random import randint

class Solution:

    def __init__(self, N, blacklist):
        blackset = set(blacklist)
        self.length = N - len(blacklist)
        i = self.length
        self.map = {}
        for num in blacklist:
            if num < N - len(blacklist):
                while i in blackset:
                    i += 1
                self.map[num] = i
                i += 1


    def pick(self):
        ind = randint(0, self.length - 1)
        if ind in self.map:
            return self.map[ind]
        return ind
