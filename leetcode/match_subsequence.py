# num of words that are subsequences of a string

'''
s = 'abcdef"
words = ['a', 'bb', 'ace', 'adf']

map all the char with index

check if words in that map
'''

def check_subsequence(s, words):
    c_map = {}
    for ind, c in enumerate(list(s)):
        if c not in c_map:
            c_map[c] = set()
        c_map[c].add(ind)
    count = 0
    print(c_map)
    for word in words:
        if is_sub(c_map, word):
            count += 1
    return count

def is_sub(c_map, word):
    start_ind = -1
    for c in word:
        if c not in c_map:
            return False
        elif max(c_map[c]) <= start_ind:
            return False
        else:
            start_ind =min([k for k in c_map[c] if k > start_ind])
    return True

print(check_subsequence('abcdef', ['a', 'bb', 'ace', 'cea']))
