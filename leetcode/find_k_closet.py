import bisect

def k_closet(lst, k, x):
    if k == 0: return []
    ind = bisect.bisect_left(lst, x)
    i, j = ind-1, ind
    while i >= 0 and j < len(lst):
        if abs(x - lst[i]) <= abs(x - lst[j]):
            i-= 1
        else:
            j += 1
        if (j - 1 - i) == k:
            return lst[i + 1: j]
    need = k - j + i + 1
    if i >= 0:
        return lst[i - need + 1 : ]
    else:
        return lst[0: j + need]
print(k_closet([0,0,1,2,3,3,4,7,7,8], 3, 5))
