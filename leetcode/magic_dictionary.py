class MagicDictionary:
    def __init__(self):
        self.root = TrieNode()

    def buildDict(self, dict):
        for word in dict:
            self._insert(word)

    def _insert(self, word):
        root = self.root
        for c in word:
            if c not in root.t:
                root.t[c] = TrieNode()
            root = root.t[c]
        root.boolean = True

    def search(self, word):
        return self._search(self.root, word, False)

    def _search(self, root, word, changed):
        if changed and not len(word) and root.boolean:
            return True
        elif not len(word):
            return False
        if not changed:
            for c in [chr(i) for i in range(ord("a"), ord("z") + 1)]:
                if c != word[0] and c in root.t and self._search(root.t[c], word[1:], True):
                    return True
                if c == word[0] and c in root.t and self._search(root.t[c], word[1:], False):
                    return True
        if changed:
            if word[0] not in root.t:
                return False
            return self._search(root.t[word[0]], word[1:], True)
        return False


class TrieNode:
    def __init__(self):
        self.t = {}
        self.boolean = False

md = MagicDictionary()
md.buildDict(["hello", "leetcode"])
print(md.search("hello"))
print(md.search("hhllo"))
