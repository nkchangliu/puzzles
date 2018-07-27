def buy_sell_stock(lst):
    if not lst:
        return 0
    res = [[0 for i in range(len(lst))] for j in range(3)]

    for k in range(1, 3):
        diff_max = res[k - 1][0] - lst[0]
        for i in range(1, len(lst)):
            res[k][i] = max(res[k][i - 1], lst[i] + diff_max)
            diff_max = max(diff_max, res[k - 1][i] - lst[i])
    return res[-1][-1]

print(buy_sell_stock([3, 3, 5, 0, 0, 3, 1, 4]))
