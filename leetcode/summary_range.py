def summary(lst):
    start, end = 0, 0
    res = []
    while start < len(lst) and end < len(lst):
        if end + 1 == len(lst) or lst[end] != lst[end + 1] - 1:
            if start == end:
                res.append(str(lst[start]))
            else:
                res.append(str(lst[start]) + "->" + str(lst[end]))
            start = end + 1
        end += 1
    return res

print(summary([0, 1, 2, 4, 5, 7]))
