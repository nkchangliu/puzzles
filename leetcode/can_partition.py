def can_partition(lst):
    total = sum(lst)
    if total % 2 != 0:
        return False
    target = total / 2

    lst = sorted(lst)
    cache = set()
    cache.add(0)
    new_cache = set()
    for num in lst:
        for sub_t in cache:
            new_cache.add(sub_t + num)
        cache.update(new_cache)
        new_cache = set()
    for num in cache:
        if num == target:
            return True
    return False

print(can_partition([1, 5, 5, 11]))
