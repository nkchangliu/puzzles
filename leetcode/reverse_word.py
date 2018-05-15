# give a string of words, reverse the words

def reverse_words(s):
    lst = s.split()

    if not lst:
        return ""
    start = 0
    end = len(lst) - 1
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    return ' '.join(lst)


print(reverse_words("   a   b "))


