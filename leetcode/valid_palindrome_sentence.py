def is_palindrome(sentence):
    sentence = sentence.lower()
    i, j = 0, len(sentence) - 1
    while i < j:
        while i < j and not (sentence[i].isalpha() or sentence[i].isdigit()):
            i += 1
        while i < j  and not (sentence[j].isalpha() or sentence[j].isdigit()):
            j -= 1
        print(i)
        print(j)
        if sentence[i] != sentence[j]:
            return False
        else:
            i += 1
            j -= 1
    return True

print(is_palindrome("ab2a"))
