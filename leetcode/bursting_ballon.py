def ballon_arrow(ballons):
    count = 0
    lst = sorted(ballons, key = lambda x: (x[1], x[0]))
    i = 0
    while i < len(lst):
        start, end = lst[i]
        count += 1
        j = i + 1
        while j < len(lst) and  lst[j][0] <= end:
            j += 1
        i = j
    return count

print(ballon_arrow([[10,16], [2,8], [1,6], [7,12]]))

