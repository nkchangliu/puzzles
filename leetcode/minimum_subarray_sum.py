def minimum_subarray(lst, s):
    i, j = 0, 0
    length, sum = float("inf"), 0
    while i < len(lst) and j < len(lst):
        sum += lst[j]
        while sum >= s:
            length = min(length, j - i + 1)
            sum -= lst[i]
            i += 1
        j += 1
    return length

print(minimum_subarray([2, 3, 1, 2, 4, 3], 7))
