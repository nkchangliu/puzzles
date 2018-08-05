def boat_to_save(lst, limit):
    lst = sorted(lst)
    start, end = 0, len(lst) - 1
    count = 0
    while start <= end:
        count += 1
        if lst[start] + lst[end] <= limit:
            start += 1
        end -= 1
    return count


print(boat_to_save([2,49,10,7,11,41,47,2,22,6,13,12,33,18,10,26,2,6,50,10],50))
