def check_word(word, pattern):
    map = {}
    value = set()
    for i in range(len(word)):
        if pattern[i] not in map:
            map[pattern[i]] = word[i]
            if word[i] in value:
                return False
            value.add(word[i])
        else:
            if map[pattern[i]] != word[i]:
                return False
    return True

def check_words(words, pattern):
    res = []
    for word in words:
        if check_word(word, pattern):
            res.append(word)
    return res

print(check_words(["abc","deq","mee","aqq","dkd","ccc"], "abb"))
