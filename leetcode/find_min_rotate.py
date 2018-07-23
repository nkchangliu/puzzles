def find_min_rotate(lst):
    s, e = 0, len(lst) - 1
    while s < e:
        if lst[s] < lst[e]:
            return lst[s]
        mid = (e + s) // 2
        if lst[mid] >= lst[s]:
            s = mid + 1
        else:
            e = mid
    return lst[s]

print(find_min_rotate([4, 5, 6, 7, 0, 1, 2]))
