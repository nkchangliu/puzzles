class MyCircularDeque:

    def __init__(self, k):
        self.first = []
        self.second = []
        self.size = 0
        self.k = k

    def insertfront(self, value):
       if not self.isfull():
           self.first.append(value)
           self.size += 1
           return True
       return False

    def insertlast(self, value):
        if not self.isfull():
           self.second.append(value)
           self.size += 1
           return True
        return False

    def deletefront(self):
        if self.isempty():
           return False
        if not self.first:
            self.first = list(reversed(self.second[0: len(self.second)//2 + 1]))
            self.second = self.second[len(self.second)//2 + 1:]
        self.first.pop()
        self.size -= 1
        return True

    def deletelast(self):
        if self.isempty():
            return False
        if not self.second:
            self.second = list(reversed(self.first[0: len(self.first)//2 + 1]))
            self.first = self.first[len(self.first)//2+1: ]
        self.second.pop()
        self.size -= 1
        return True

    def getfront(self):
        if self.isempty():
           return -1
        if not self.first:
             return self.second[0]
        else:
             return self.first[-1]

    def getrear(self):
        if self.isempty():
           return -1
        if not self.second:
             return self.first[0]
        else:
             return self.second[-1]

    def isempty(self):
       return self.size == 0

    def isfull(self):
        return self.size == self.k


