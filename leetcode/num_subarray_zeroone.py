def num_subarray(A, S):
    indexes = []
    for i, val in enumerate(A):
        if val:
            indexes.append(i)
    count = 0
    if len(indexes) == S: return 1
    for lo in range(len(indexes) - S + 1):
        # lo is the start ind, lo+s-1 is the end index
        if lo == 0:
            count += indexes[lo+S] - indexes[lo+S-1]
        elif lo + S >= len(indexes):
            count += indexes[lo] - indexes[lo - 1]
        else:
            count += (indexes[lo] - indexes[lo-1]) * (indexes[lo+S] - indexes[lo+S-1])
    return count


print(num_subarray([1, 0, 1, 0, 1, 0, 0, 0, 1], 3))
