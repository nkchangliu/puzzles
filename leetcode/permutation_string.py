import collections

def permutation(str1, str2):
    s1_map = collections.Counter(str1)
    s2_map = collections.Counter(str2[0: len(str1)])

    if s1_map == s2_map:
        return True
    for i in range(len(str2) - len(str1)):
        s2_map[str2[i]] -= 1
        if s2_map[str2[i]] == 0:
            del s2_map[str2[i]]
        if str2[i + len(str1)] not in s2_map:
            s2_map[str2[i + len(str1)]] = 0
        s2_map[str2[i + len(str1)]] += 1

        if s1_map == s2_map:
            return True
    return False

print(permutation("adc","edcda"))
