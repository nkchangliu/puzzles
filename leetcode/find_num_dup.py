def find_dup(lst):
    res = []
    for num in lst:
        if lst[abs(num) - 1] < 0:
            res.append(abs(num))
        else:
            lst[abs(num) - 1] *= -1
    return res

print(find_dup([4, 3, 2, 7, 8, 2, 3, 1]))
