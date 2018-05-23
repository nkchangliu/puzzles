def rob_lst(lst):
    if not lst:
        return 0
    elif len(lst) == 1:
        return lst[0]
    elif len(lst) == 2:
        return max(lst[0], lst[1])
    # suppose house 0 is not robbed
    z_value = rob(lst[1:])
    # suppose house 1 is not robbed
    f_value = rob(lst[2:] + lst[0:1])
    return max(z_value, f_value)



def rob(lst):
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

print(rob_lst([3, 4, 5,2, 1, 3, 5]))
