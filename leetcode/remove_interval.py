def discard_interval(lst):
    lst = sorted(lst, key = lambda x: x[0])
    start = count = 0
    while start < len(lst):
        j = start + 1
        while j < len(lst) and lst[j][0] < lst[start][1]:
            count += 1
            if lst[j][1] < lst[start][1]:
                start = j
            j += 1
        start = j
    return count

print(discard_interval([ [1,2], [2,3], [3,4], [1,3] ]))

