def remove_dup(lst):
    if len(lst) <= 1:
        return lst
    i, j = 1, 1
    while i < len(lst) and j < len(lst):
        if lst[j] != lst[i - 1]:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j += 1
        else:
            j += 1
    return i

print(remove_dup([1, 1, 2, 3, 3, 4, 5]))
