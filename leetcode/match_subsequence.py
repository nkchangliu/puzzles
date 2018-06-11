# num of words that are subsequences of a string

'''
s = 'abcdef"
words = ['a', 'bb', 'ace', 'adf']

map all the char with index

check if words in that map
'''
import bisect

def check_subsequence(s, words):
    c_map = {}
    for ind, c in enumerate(list(s)):
        if c not in c_map:
            c_map[c] = []
        c_map[c].append(ind)

    for key in c_map:
        c_map[key] = sorted(c_map[key])
    count = 0
    for word in words:
        if is_sub(c_map, word):
            count += 1
    return count

def is_sub(c_map, word):
    start_ind = -1
    for c in word:
        if c not in c_map:
            return False
        c_ind = bisect.bisect_right(c_map[c], start_ind)
        if c_ind >= len(c_map[c]):
            return False
        else:
            start_ind = c_map[c][c_ind]
    return True

print(check_subsequence('aabcddef', ['a', 'bb', 'ace', 'cea']))
