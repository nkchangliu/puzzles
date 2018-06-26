def combination(nums, target):
    cache = {}
    cache[0] = 1
    return combination_sum(nums, target, cache)


def combination_sum(nums, target, cache):
    if target in cache:
        return cache[target]
    res = 0
    for num in nums:
        if target >= num:
            res += combination_sum(nums, target - num, cache)
    cache[target] = res
    return res


def combination_dp(nums, target):
    ans = [0] * (target + 1)
    ans[0] = 1
    for i in range(1, target + 1):
        for num in nums:
            if i >= num:
                ans[i] += ans[i - num]
    return ans[target]


print(combination_dp([1, 2, 3], 4))
