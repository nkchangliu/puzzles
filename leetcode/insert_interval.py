class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def not_overlap(lst, new_interval):
    if new_interval.end < lst[0].start:
        return 0
    for i in range(1, len(lst)):
        if lst[i-1].end < new_interval.start and lst[i].start > new_interval.end:
            return i
    if new_interval.start > lst[-1].end:
        return len(lst)
    return - 1

def find_interval(lst, new_interval):
    overlap = False
    left, right = 0, len(lst)
    for i in range(len(lst)):
        start, end = lst[i].start, lst[i].end
        if start <= new_interval.end and new_interval.start <= end:
            if not overlap:
                left = i
                overlap = True
        else:
            if overlap:
                return left, i
    return left, right

def insert_interval(lst, new_lst):
    if not lst:
        return [new_lst]
    index = not_overlap(lst, new_lst)
    if index != - 1:
        lst.insert(index, new_lst)
    else:
        left, right = find_interval(lst, new_lst)
        new_lst = Interval(min(new_lst.start, lst[left].start), max(new_lst.end, lst[right - 1].end))
        del lst[left: right]
        lst.insert(left, new_lst)
    return lst
