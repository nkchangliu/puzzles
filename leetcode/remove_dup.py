def remove_dup(lst):
    lst.sort()
    i = 0
    for j in range(len(lst)):
        if lst[i] != lst[j]:
            lst[i + 1], lst[j] = lst[j], lst[i + 1]
            i += 1
    for j in range(len(lst) - i - 1):
        lst.pop()
    return lst

print(remove_dup([3, 1, 2, 1, 3, 2, 2, 2, 4, 5, 4, 5, 5]))

