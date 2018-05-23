def longest_increasing(lst):
    if len(lst) <= 1:
        return len(lst)
    cache = [1] * len(lst)
    for i in range(1, len(lst)):
        max_sub_len = 1
        for j in range(0, i):
            if lst[i] > lst[j]:
                value = cache[j] + 1
                if value > max_sub_len:
                    max_sub_len = value
        cache[i] = max_sub_len

    return max(cache)

