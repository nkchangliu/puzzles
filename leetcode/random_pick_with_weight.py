import bisect
from random import randint
class Solution:

    def __init__(self, w):
        start = 0
        lst = []
        for num in w:
            start += num
            lst.append(start)
        self.lst = lst
        self.val = start

    def pickIndex(self):
        val = randint(1, self.val)
        return bisect.bisect_left(self.lst, val)


