def buy_w_fee(lst, fee):
    res = [0] * len(lst)

    for i in range(1, len(lst)):
        max_profit_with_i = max(lst[i] - lst[buy] - fee + res[buy] for buy in range(0, i))
        res[i] = max(max_profit_with_i, res[i - 1])
    return res[-1]

def buy_w_fee_2(lst, fee):
    cash, hold  = 0, -lst[0]
    for i in range(1, len(lst)):
        cash = max(cash, hold + lst[i] - fee)
        hold = max(hold, cash - lst[i])
    return cash

print(buy_w_fee_2([1, 3, 2, 8, 4, 9], 2))
