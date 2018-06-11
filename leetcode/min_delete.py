def min_delete(s1, s2):
    num = lcs(s1, s2)
    return len(s1) + len(s2) - 2 * num


def lcs(s1, s2):
    cache = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                cache[i][j] = cache[i - 1][j - 1] + 1
            else:
                cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])
        print(cache)
    return cache[len(s1)][len(s2)]

print(min_delete("sea", "eat"))
