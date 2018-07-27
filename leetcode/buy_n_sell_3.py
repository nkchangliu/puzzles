def buy_sell_stock(lst):
    res = [[0 for i in range(len(lst))] for j in range(3)]

    for k in range(1, 3):
        for i in range(1, len(lst)):
            include_max = 0
            for index in range(i - 1, -1, -1):
                include_max = max(include_max, lst[i] - lst[index] + res[k - 1][index])

            res[k][i] = max(res[k][i - 1], include_max)
    return res[-1][-1]

print(buy_sell_stock([3, 3, 5, 0, 0, 3, 1, 4]))
