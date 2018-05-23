def set_mismatch(nums):
    cache = set()
    dup, miss = None, None
    for num in nums:
        if num not in cache:
            cache.add(num)
        else:
            dup = num

    for i in range(1, len(nums) + 1):
        if i not in cache:
            miss = i

    return [dup, miss]


print(set_mismatch([1, 2, 2, 4]))
