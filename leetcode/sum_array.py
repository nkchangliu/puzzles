def sum_array(lst, k):
    return _sum_array(lst, k, len(lst) - 1, 3, {})


def _sum_array(lst, k, end, groups, cache):
    if groups < 1 or k * groups > end + 1:
        return 0, []
    if (end, groups) in cache:
        return cache[(end, groups)]

    not_include_val, not_include_lst = _sum_array(lst, k, end - 1, groups, cache)
    include_val, include_lst = _sum_array(lst, k, end - k, groups - 1, cache)

    if include_val + sum(lst[end - k: end + 1]) >= not_include_val:
        cache[(end, groups)] = (include_val+ sum(lst[end - k : end + 1]), include_lst.append(end - k))
    else:
        cache[(end, groups)] = (not_include_val, not_include_lst)
    print(cache)
    return cache[(end, groups)]



def sum_array_dp(lst, k):
    res = [[(0, []) for i in range(len(lst))] for j in range(4)]

    for j  in range(1, len(lst)):
        for i in range(1, 4):
            not_include_val, not_include_lst = res[i][j - 1]
            res[i][j] = res[i][j - 1]
            if j - k + 1 >= 0:
                include_val, include_lst = res[i - 1][j - k]
                if include_val + sum(lst[j - k + 1: j + 1]) > not_include_val:
                    new_lst = include_lst + [j - k + 1]
                    res[i][j] = (include_val + sum(lst[j - k + 1: j + 1]), new_lst)
    return res[3][len(lst) - 1][1]

print(sum_array_dp([1,2,1,2,6,7,5,1], 2))
