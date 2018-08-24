def can_win(max_num, target):
    if (1 + max_num) * max_num // 2 < target:
        return False
    s = [x for x in range(1, max_num + 1)]
    return _can_win(s, target, {})

def _can_win(s, target, cache):
    hash = "".join([str(x) for x in s])
    if hash in cache:
        return cache[hash]
    if s and s[-1] >= target:
        return True
    for i in range(len(s)):
        num = s[i]
        if num <= target and not _can_win(s[0: i] + s[i + 1:], target - num, cache):
            cache[hash] = True
            return True
    cache[hash] = False
    return False
