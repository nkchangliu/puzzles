class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.map = {}

    def insert(self, word, val):
        old_val = self.map[word] if word in self.map else 0
        self.map[word] = val
        update_val = val - old_val
        root = self.root
        for c in word:
            if c not in root.t:
                root.t[c] = TrieNode()
            root.val += update_val
            root = root.t[c]
        root.val += update_val
        root.boolean = True

    def sum(self, prefix):
        root = self.root
        for c in prefix:
            if c not in root.t:
                return 0
            root = root.t[c]
        return root.val

class TrieNode:
    def __init__(self, val = 0):
        self.t = {}
        self.val = val
        self.boolean = False


