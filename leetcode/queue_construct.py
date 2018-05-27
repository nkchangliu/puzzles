def construct_queue(lst):
    res = []
    for num in reversed(sorted(lst, key = lambda pair: (pair[0], -pair[1]))):
        res.insert(num[1], num)
    return res

print(construct_queue([[4, 4], [5, 0], [7,0], [7, 1], [6, 1], [5, 2]]))
