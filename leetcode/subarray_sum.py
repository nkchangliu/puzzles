def subarray_sum(lst, k):
    sum_map = {}
    count, total = 0, 0

    for num in lst:
        total += num
        if total - k in sum_map:
            count += sum_map[total - k]
        if total not in sum_map:
            sum_map[total] = 1
        else:
            sum_map[total] = sum_map[total] + 1
    return count

print(subarray_sum([1, 1, 2, 3, 1, 4, 1], 5))
