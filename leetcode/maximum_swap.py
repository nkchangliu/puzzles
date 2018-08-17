def maximum_swap(num):
    if not num:
        return 0
    lst = [int(x) for x in str(num)]

    max_right_most=[(lst[-1], len(lst)-1)] * (len(lst))
    for i in range(len(lst) - 2, -1, -1):
        if lst[i + 1] > max_right_most[i + 1][0]:
            max_right_most[i] = (lst[i + 1], i+ 1)
        else:
            max_right_most[i] = max_right_most[i + 1]
    for i in range(len(lst) - 1):
        if lst[i] < max_right_most[i][0]:
            lst[i], lst[max_right_most[i][1]] = lst[max_right_most[i][1]], lst[i]
            return int("".join([str(x) for x in lst]))
    return num

print(maximum_swap(2789))

