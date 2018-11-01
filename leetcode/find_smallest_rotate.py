def find_smallest(lst):
    if not lst: return None
    if lst[0] < lst[-1]:
        return lst[0]
    lo, hi = 0, len(lst) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid == 0:
            lo = mid + 1
        elif lst[mid] < lst[mid - 1]:
            return lst[mid]
        elif lst[mid] >= lst[lo]:
            lo = mid + 1
        else:
            hi = mid - 1

print(find_smallest([2, 2, 2, 0, 1]))
