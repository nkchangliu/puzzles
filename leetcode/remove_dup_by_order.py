def remove_dup(lst):
    cache = {}
    for i in range(len(lst)):
        cache[lst[i]] = i
    last_ind = 0
    res = ''
    while cache:
        print(cache)
        min_ind = min(cache.values())
        ind = find_min_ele(cache, lst, last_ind, min_ind)
        res += lst[ind]
        del cache[lst[ind]]
        last_ind = ind + 1
    return res

def find_min_ele(cache, lst, last_ind, min_ind):
    target_ind = None
    for ind in range(last_ind, min_ind + 1):
        if lst[ind] in cache and (target_ind is None or lst[ind] < lst[target_ind]):
            target_ind = ind
    return target_ind

print(remove_dup("ccacbaba"))
