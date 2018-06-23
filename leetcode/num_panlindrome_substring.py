def palindrome_substring(s):
    cache = [[False for i in range(len(s))] for j in range(len(s))]
    count = 0
    for i in range(len(s)):
        cache[i][i] = True
        count += 1
    for i in range(len(s)-1, -1, -1):
        for j in range(i + 1, len(s)):
            if i + 1 == j and s[i] == s[j]:
                cache[i][j] = True
                count += 1
            elif s[i] == s[j] and cache[i+1][j-1]:
                cache[i][j] = True
                count += 1
    return count

print(palindrome_substring('agbdba'))

