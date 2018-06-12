def largest_divisible(lst):
    path = {}
    subset_len = {}
    sorted_lst = sorted(lst)

    for i in range(len(lst)):
        max_len = 0
        max_index = i
        for j in range(i):
            if sorted_lst[i] % sorted_lst[j] == 0:
                if subset_len[j] > max_len:
                    max_len = subset_len[j]
                    max_index = j
        subset_len[i] = max_len + 1
        path[i] = max_index
    max_ind = max(subset_len, key = subset_len.get)

    res = []
    while max_ind in path and path[max_ind] != max_ind:
        res.append(sorted_lst[max_ind])
        max_ind = path[max_ind]
    res.append(sorted_lst[max_ind])

    return [i for i in reversed(res)]

print(largest_divisible([1, 2, 3, 4, 6, 7]))
