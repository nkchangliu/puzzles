def longest_chain(lst):
    lst = sorted(lst, key = lambda x: x[1])
    i = j = length = 0
    while i < len(lst):
        while j < len(lst) and lst[j][0] <= lst[i][1]:
            j += 1
        length += 1
        i = j
    return length




print(longest_chain([[1, 2],[3, 4], [1, 4], [2, 3]]))
