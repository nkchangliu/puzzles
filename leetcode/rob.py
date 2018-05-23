def rob(lst):
    if not lst:
        return 0
    if len(lst) == 1:
        return lst[0]

    res = [(0)] * len(lst)
    res[0] = lst[0]
    res[1] = lst[1] if lst[1] > lst[0] else lst[0]
    for i in range(2, len(lst)):
        if lst[i] + res[i - 2] > res[i - 1]:
            res[i] = lst[i] + res[i - 2]
        else:
            res[i] = res[i - 1]
    return res[len(lst) - 1]


print(rob([1, 3, 4, 2, 1]))
