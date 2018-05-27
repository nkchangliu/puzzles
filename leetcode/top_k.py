def top_k_elements(lst, k):
    cache = {}
    for num in lst:
        cache[num] = 1 if num not in cache else cache[num] + 1
    sorted_cache = sorted(cache.items(), key=lambda x: x[1])
    res = []
    print(sorted_cache)
    for i in range(k):
        res.append(sorted_cache[len(sorted_cache) - i - 1][0])
    return res

print(top_k_elements([1, 1, 1, 2, 2, 3], 2))
