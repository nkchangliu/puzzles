def buy_n_sell(lst, k):
    if not lst or k == 0:
        return 0
    if k * 2 >= len(lst):
        return quick_solve(lst)
    res = [0 for i in range(len(lst))]
    for j in range(1, k + 1):
        new_res = [0 for i in range(len(lst))]
        max_diff = res[0] - lst[0]
        for i in range(1, len(lst)):
            new_res[i] = max(new_res[i - 1], lst[i] + max_diff)
            max_diff = max(max_diff, res[i] - lst[i])
        res = new_res
    return res[-1]


def quick_solve(lst):
    res = 0
    for i in range(1, len(lst)):
        if lst[i] - lst[i - 1] > 0:
            res += lst[i] - lst[i - 1]
    return res


