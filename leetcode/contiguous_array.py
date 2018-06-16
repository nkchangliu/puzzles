def contiguous(lst):
    cache = {}
    count, max_len = 0, 0
    for i in range(len(lst)):
        if lst[i] == 0:
            count += -1
        else:
            count += 1
        if count == 0:
            max_len = max(max_len, i + 1)
        elif count not in cache:
            cache[count] = i
        else:
            max_len = max(max_len, i - cache[count])
    return max_len

print(contiguous([1, 0, 1, 0, 1, 0]))

