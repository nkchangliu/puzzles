class FreqStack:

    def __init__(self):
        self.freq = {}
        self.map = {}
        self.max_freq = 0


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        freq, map = self.freq, self.map
        freq[x] = freq[x] + 1 if x in freq else 1
        if freq[x] not in map:
            map[freq[x]] = []
        map[freq[x]].append(x)
        self.max_freq = max(self.max_freq, freq[x])

    def pop(self):
        """
        :rtype: int
        """
        max_freq, freq, map = self.max_freq, self.freq, self.map
        ele = map[max_freq].pop()
        freq[ele] -= 1
        if not map[max_freq]:
            self.max_freq -= 1
        return ele
