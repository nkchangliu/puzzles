import bisect
def valid_triangle(nums):
    if len(nums) < 3:
        return 0
    count, index = 0, 2
    nums = sorted(nums)
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] != 0 and nums[j] != 0:
                index = bisect.bisect_left(nums, nums[i] + nums[j])
                count += (index - j - 1)
    return count

print(valid_triangle([2, 2, 3, 4, 5]))

