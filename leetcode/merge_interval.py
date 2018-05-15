# merge overlapping intervals in a list


def merge(lst):
    sorted_lst = sorted(lst, key = lambda x: (x[0], x[1]))
    res = []
    for interval in sorted_lst:
        if not res:
            res.append(interval)
        else:
            if overlap(res[-1], interval):
                last = res.pop()
                res.append([last[0], interval[1]])
            else:
                res.append(interval)
    return res

def overlap(interval1, interval2):
    return interval2[0] <= interval1[1]

print(merge([[1, 2], [3, 4], [1, 3], [2, 7], [9, 10]]))
