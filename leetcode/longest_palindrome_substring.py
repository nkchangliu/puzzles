def longest_palindrome(s):
    if len(s) == 0:
        return 0

    res = [[False for i in range(len(s))] for j in range(len(s))]

    longest_s, longest_e = 0, 0

    for i in range(len(s)):
        res[i][i] = True

    for i in range(len(s) -1):
        if s[i] == s[i + 1]:
            res[i][i + 1] = True
            longest = 2
            longest_s, longest_e = i, i + 1

    for j in range(2, len(s)):
        for i in range(0, j - 1):
            if res[i + 1][j - 1] and s[i] == s[j]:
                res[i][j] = True
            if res[i][j] and j - i > longest_e - longest_s:
                longest_s = i
                longest_e = j
    return s[longest_s : longest_e + 1]

def expand_around(s):
    if len(s) == 0:
        return 0

    start, end = 0, 0
    for i in range(len(s) - 1):
        len1 = expand(s, i, i)
        len2 = expand(s, i, i + 1)
        length = max(len1, len2)
        if length > end - start + 1:
            start = i - (length - 1) // 2
            end = i + length // 2
    return s[start : end + 1]

def expand(s, i, j):
    while i >= 0 and j < len(s):
        if s[i] == s[j]:
            i -= 1
            j += 1
        else:
            break
    return j - i - 1

print(expand_around("abbbac"))
