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



def sum_array_dp(lst, sum_lst, k):
    res = [[0 for i in range(len(lst))] for j in range(4)]

    for j  in range(1, len(lst)):
        for i in range(1, 4):
            res[i][j] = res[i][j - 1]
            if j - k + 1 >= 0:
                if res[i - 1][j - k] + sum_lst[j + 1] - sum_lst[j - k + 1] > res[i][j - 1]:
                    res[i][j] = res[i - 1][j - k] + sum_lst[j + 1] - sum_lst[j - k + 1]
    return res

def prefix_sum(lst):
    sum_lst = [0]
    prefix_s = 0
    for num in lst:
        prefix_s +=  num
        sum_lst.append(prefix_s)
    return sum_lst

def get_path(lst, k):
    sum_lst = prefix_sum(lst)
    res = sum_array_dp(lst, sum_lst, k)
    path = []
    i, j = 3, len(lst) - 1
    while i > 0 and j > 0:
        if res[i - 1][j - k ] + sum_lst[j + 1] - sum_lst[j - k + 1] > res[i][j - 1]:
            path.append(j - k + 1)
            j = j - k
            i -= 1
        else:
            j -= 1
    return path[::-1]

print(get_path([1,2,1,2,6,7,5,1], 2))
