# check if the word can be represented use words from word dict

def word_break(word, worddict):
    last_index = [0]
    for i in range(1, len(word) + 1):
        for index in last_index:
            if word[index:i] in worddict:
                last_index.append(i)
                break
    return last_index[-1] == len(word)

print(word_break("applepenapple", set(["apple", "pen"])))

