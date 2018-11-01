def reverse_letters(S):
    res = [None] * len(S)
    chars = []
    for i in range(len(S)):
        if S[i].isalpha():
            chars.append(S[i])
        else:
            res[i] = S[i]
    print(chars)
    print(res)
    i = 0
    j = len(chars) - 1
    while i < len(res):
        if res[i] is None:
            res[i] = chars[j]
            j -= 1
        i += 1
    return "".join(res)

print(reverse_letters("Test1ng-Leet=code-Q!"))
