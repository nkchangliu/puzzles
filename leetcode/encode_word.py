ENDS_HERE = '__ENDS_HERE'

class Trie(object):

    def __init__(self):
        self._trie = {}


    def insert(self, text):
        trie = self._trie
        for char in text:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie[ENDS_HERE] = True

    def contain_length(self, text):
        trie = self._trie
        length = 0
        for char in text:
            if char in trie:
                trie = trie[char]
                length += 1
            else:
                return -1
            if ENDS_HERE in trie and len(trie) == 1:
                return length
        return length

def encode(words):
    trie = Trie()
    total = 0
    for word in words:
        reversed_word = word[::-1]
        length = trie.contain_length(reversed_word)
        trie.insert(reversed_word)
        total += len(word) - length
    return total
