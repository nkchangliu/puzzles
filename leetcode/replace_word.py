def replace_word(roots, sentence):
    sentence = sentence.split(" ")
    for i in range(len(sentence)):
        for root in roots:
            if sentence[i].startswith(root):
                sentence[i] = root
    return (" ").join(sentence)

print(replace_word(["cat", "bat", "rat"], "the cattle was rattled by the battery"))


