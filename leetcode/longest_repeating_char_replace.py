def longest_repeating(lst, k):
    cache = {}
    max_length = 0
    start, end, max_count = 0, 0, 0
    while end < len(lst):
        cache[lst[end]] = cache[lst[end]] + 1 if lst[end] in cache else 1
        max_count = max(cache.values())

        if max_count + k > end - start:
            max_length = max(max_length, end - start + 1)
            end += 1
        else:
            cache[lst[start]] -= 1
            cache[lst[end]] -= 1
            start += 1
    return max_length

print(longest_repeating("ABAB", 2))
