def search_rotate(lst, target):
    lo, hi = 0, len(lst) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if target == lst[mid]:
            return mid
        if lst[lo] < lst[hi]:
            if target < lst[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if lst[mid] >= lst[lo] and target >= lst[lo] and target < lst[mid]:
                hi = mid - 1
            elif lst[mid] >= lst[lo]:
                lo = mid + 1
            elif lst[mid] < lst[lo] and target > lst[mid] and target <= lst[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1

print(search_rotate([4, 5, 6, 7, 0, 1, 2], 4))
