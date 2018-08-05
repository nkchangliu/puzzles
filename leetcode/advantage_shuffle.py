import bisect

def advantage_shuffle(lst_a, lst_b):
    lst_a.sort()
    res = []
    for num in lst_b:
        i = bisect.bisect_right(lst_a, num)
        j = i if i < len(lst_a) else 0
        res.append(lst_a[j])
        lst_a.pop(j)

    return res


def advantage_shuffle_faster(lst_a, lst_b):
    lst_a.sort()
    lst_b = sorted([(num, i) for i, num  in enumerate(lst_b)])
    i, j = 0, 0
    not_used = []
    res = [None] * len(lst_a)

    while i < len(lst_a) and j < len(lst_b):
        if lst_a[i] > lst_b[j][0]:
            res[lst_b[j][1]] = lst_a[i]
            j += 1
        else:
            not_used.append(lst_a[i])
        i += 1

    j = 0
    for i in range(len(res)):
        if res[i] is None:
            res[i] = not_used[j]
            j += 1
    return res

print(advantage_shuffle_faster([2,7,11,15], [1,10,4,11]))
