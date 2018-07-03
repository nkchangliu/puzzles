EOW = '__END__OF_WORD__'
class Trie(object):

    def __init__(self):
        self.trie = {}

    def insert(self, word):
        trie = self.trie
        for c in word:
            if c not in trie:
                trie[c] = {}
            trie = trie[c]
        trie[EOW] = True

    def search(self, word):
        trie = self.trie
        for c in word:
            if c in trie:
                trie = trie[c]
            else:
                return False
        return trie[EOW]

    def prefix(self, word):
        trie = self.trie
        for c in word:
            if c in trie:
                trie = trie[c]
            else:
                return False
        return True

