def repeated_sequence(s):
    cache = set()
    res = set()
    for i in range(len(s) - 9):
        sub_string = s[i: i + 10]
        if sub_string in cache:
            res.add(sub_string)
        else:
            cache.add(sub_string)

    return list(res)

print(repeated_sequence("AAAAAAAAAAA"))
