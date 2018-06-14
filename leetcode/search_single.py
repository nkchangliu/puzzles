def search(lst):
    if len(lst) < 2:
        return lst
    start, end = 0, len(lst) - 1
    while start < end:
        mid = (end - start) // 2 + start
        if lst[mid] == lst[mid + 1]:
            if (mid - start) % 2 == 0:
                start = mid + 2
            else:
                end = mid - 1
        elif lst[mid] == lst[mid - 1]:
            if (mid - start) % 2 == 0:
                end = mid - 2
            else:
                start = mid + 1
        else:
            return lst[mid]
    return lst[start] if start >= 0 and start < len(lst) else lst[end]

print(search([1, 1, 2, 4, 4,8, 8]))
