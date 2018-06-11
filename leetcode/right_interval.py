import bisect

def right_interval(lst):
    cache = {}
    for num, interval in enumerate(lst):
        start = interval[0]
        cache[start] = num
    sorted_dict = sorted(cache)
    res = []
    for num, interval in enumerate(lst):
        end = interval[1]
        ind = bisect.bisect_left(sorted_dict, end)
        if ind >= len(lst) or cache[sorted_dict[ind]] == num:
            res.append(-1)
        else:
            res.append(cache[sorted_dict[ind]])

    return res
print(right_interval([[1, 2], [2, 3]]))
