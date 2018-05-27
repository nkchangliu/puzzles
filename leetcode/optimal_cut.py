def cutpoint(matrix):
    stop = {}
    for lst in matrix:
        count = 0
        for num in lst:
            count += num
            stop[count] = 1 if count not in stop else stop[count] + 1
    max_key = max(stop, key = lambda x: stop[x])
    lst = [k for k in stop if k != max_key]
    if len(lst) == 1:
        return len(matrix)
    key = max(lst, key = lambda x: stop[x])
    return len(matrix) - stop[key]

