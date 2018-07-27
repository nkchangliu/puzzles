def buy_n_sell(lst, k):
    if not lst or k == 0:
        return 0
    res = [[0 for i in range(len(lst))] for j in range(k + 1)]
    for j in range(1, k + 1):
        max_diff = res[j - 1][0] - lst[0]
        for i in range(1, len(lst)):
            res[j][i] = max(res[j][i - 1], lst[i] + max_diff)
            max_diff = max(max_diff, res[j - 1][i] - lst[i])
    return res[-1][-1]



