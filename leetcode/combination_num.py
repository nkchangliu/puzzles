def combinations(k, n):
    lst = [x for x in range(1, 10)]

    return helper(lst, k, n)

def helper(lst, k , n):
    if k == 0 and n == 0:
        return [[]]
    elif n == 0 or k == 0:
        return []
    res = []
    for num in lst:
        if num <= n:
            new_lst = [x for x in lst if x > num]
            sub_res = helper(new_lst, k - 1, n - num)
            res += [x + [num] for x in sub_res]
    return res


print(combinations(3, 9))
