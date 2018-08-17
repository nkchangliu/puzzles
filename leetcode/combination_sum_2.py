def candidate_sum(lst, target):
    lst.sort()
    res = _candidate_sum(lst, 0, target, {})
    return [list(x) for x in set(res)]

def _candidate_sum(lst, start, target, cache):
    if start >= len(lst) and target != 0:
        return []
    if target == 0:
        return [()]
    if (start, target) in cache:
        return cache[(start, target)]
    res = []
    print(cache)
    for j in range(start, len(lst)):
        if lst[j] <= target:
            sub_res = _candidate_sum(lst, j + 1, target - lst[j], cache)
            res += [x + (lst[j],) for x in sub_res]
    cache[(start, target)] = res
    return res

print(candidate_sum([10,1,2,7,6,1,5], 8))
