def longest_word(dicts, words):
    longest_word = ""
    for word in words:
        if is_subsequence(dicts, word):
            if len(word) > len(longest_word) or (len(word) == len(longest_word) and word < longest_word):
                longest_word = word

    return longest_word

def is_subsequence(dicts, word):
    i, j = 0, 0
    while i < len(dicts) and j < len(word):
        if dicts[i] == word[j]:
            j += 1
        i += 1
    return j == len(word)


print(longest_word("afandraynlrnsalmx", ["apple", "afand", "adransalmx"]))
