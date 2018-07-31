def longest_sub_string(s):
    dict = {}
    i, j = 0, 0
    length = 0
    while j < len(s):
        if s[j] in dict and max(dict[s[j]]) >= i:
            i = max(dict[s[j]]) + 1
        else:
            if s[j] not in dict:
                dict[s[j]] = set()
            dict[s[j]].add(j)
            length = max(length, j - i + 1)
            j += 1
    return length


print(longest_sub_string("abcabcbb"))
