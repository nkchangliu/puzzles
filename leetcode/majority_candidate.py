def majority(nums):
    candidate, count = None, 0

    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
    return candidate

print(majority([2,1,2,1,2]))
