def longest(s):
    if len(s) == 0:
        return 0

    cache = [[1 for i in range(len(s))] for j in range(len(s))]

    for i in range(len(s)-1, -1, -1):
        for j in range(i+1, len(s)):
            if j == i + 1 and s[i] == s[j]:
                cache[i][j] = 2
            elif s[i] == s[j]:
                cache[i][j] = 2 + cache[i+1][j-1]
            else:
                cache[i][j] = max(cache[i+1][j], cache[i][j-1])
    return cache[0][-1]


print(longest("bbbab"))

