import collections

def delete_n_earn(lst):
    if not lst:
        return 0
    count_map = collections.Counter(lst)
    keys = sorted(list(count_map))

    ans = [0] * len(keys)
    ans[0] = keys[0] * count_map[keys[0]]
    for i in range(1, len(keys)):
        not_use = ans[i - 1]
        use = keys[i] * count_map[keys[i]]
        if keys[i] != keys[i - 1] + 1:
            use += ans[i - 1]
        elif i >= 2:
            use += ans[i - 2]
        ans[i] = max(use, not_use)

    return ans[-1]

print(delete_n_earn([3, 2, 4]))
