
def longest_substring(s, k):
    return _longest_substring(s, 0, len(s) - 1, k)

def _longest_substring(s, start, end, k):
    if start > end:
        return 0
    cache = make_cache(s, start, end)
    for key in cache:
        if len(cache[key]) < k:
            for ind in cache[key]:
                left = _longest_substring(s, start, ind - 1, k)
                right = _longest_substring(s, ind + 1, end, k)
                return max(left, right)
    return end - start + 1


def make_cache(s, start, end):
    cache = {}
    for i in range(start, end + 1):
        if s[i] not in cache:
            cache[s[i]] = set()
        cache[s[i]].add(i)

    return cache


print(longest_substring("ababbbc", 2))
