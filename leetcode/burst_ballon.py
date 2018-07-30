def burst_ballon(lst):
    nums = [1] + [x for x in lst if x > 0] + [1]
    return helper(nums, 0, len(nums) - 1, {})

def helper(nums, left, right, cache):
    if left + 1 == right:
        return 0
    if (left, right) in cache:
        return cache[(left, right)]
    res = 0
    for i in range(left+1, right):
        res = max(res, nums[left] * nums[right] * nums[i] + helper(nums, left, i, cache) + helper(nums, i, right, cache))
    cache[(left, right)] = res
    return cache[(left, right)]

print(burst_ballon([3, 1, 5, 8]))
