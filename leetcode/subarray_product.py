def subarray_product(nums, k):
    i, j, product, count =0, 0, 1, 0
    while i < len(nums) and j < len(nums):
        product *= nums[j]
        while i < j and product >= k:
            product = product // nums[i]
            i += 1
        if product < k:
            count += j - i + 1
        j += 1
    return count

print(subarray_product([10, 5, 2, 6], 100))


