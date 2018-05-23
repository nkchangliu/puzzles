def target_sum(lst, s):
    if len(lst) == 0 and s == 0:
        return 1
    elif len(lst) == 0:
        return 0

    cache = {}
    cache[lst[0]] = 1
    cache[-lst[0]] = 1
    if lst[0] == 0:
        cache[0] = 2

    for i in range(1, len(lst)):
        new_cache = {}
        for key in cache:
            new_key = key + lst[i]
            new_cache[new_key] = cache[key] if new_key not in new_cache else new_cache[new_key] + cache[key]

            new_key = key - lst[i]
            new_cache[new_key] = cache[key] if new_key not in new_cache else cache[key] + new_cache[new_key]

        cache = new_cache

    return cache[s] if s in cache else 0

print(target_sum([1, 1, 1, 1, 1], 3))
