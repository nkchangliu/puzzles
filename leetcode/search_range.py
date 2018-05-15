# given a list and a target, search for the start and the end index of the target

def search_range(nums, target):
    mid, start, end = binary_search(nums, target)

    if start == end:
        return [start, end]

    target_start = search_start(nums, target, start, mid)
    target_end = search_end(nums, target, mid, end)

    return [target_start, target_end]


def binary_search(nums, target):
    if len(nums) == 0:
        return -1, -1, -1
    start = 0
    end = len(nums) - 1

    while start < end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid, start, end
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    if nums[start] == target:
        return start, start, start
    return -1, -1, -1

def search_start(nums, target, start, end):
    while start < end:
        mid = (start + end) // 2
        if nums[mid] == target:
            end = mid - 1
        else:
            start = mid + 1
    if nums[start] == target:
        return start
    return start + 1

def search_end(nums, target, start, end):
    while start < end:
        mid = (start + end) // 2
        if nums[mid] == target:
            start = mid + 1
        else:
            end = mid - 1
    if nums[start] == target:
        return start
    return start - 1

print(search_range([2, 3, 4, 6, 6, 6, 7, 8, 10, 12, 14], 6))


