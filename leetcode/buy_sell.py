def buy_sell(lst):
    if len(lst) <= 1:
        return 0
    res = [0] * len(lst)

    for i in range(1, len(lst)):
        not_sell = res[i - 1]
        sell = 0
        for j in range(i):
            profit = lst[i] - lst[j]
            if j - 2 >= 0:
                profit += res[j - 2]
            if profit > sell:
                sell = profit
        res[i] = max(not_sell, sell)

    return res[-1]

print(buy_sell([1, 2, 3, 0, 2]))
