def largest_histogram(lst):
    cache = {}
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if i == j:
                cache[(i, j)] = i
            else:
                cache[(i, j)] = min(j, cache[i, j - 1], key=lambda x: lst[x])
    return _largest_histogram(lst, 0, len(lst) - 1, cache)

def _largest_histogram(lst, start, end, cache):
    if start > end:
        return 0
    smallest_ind = cache[(start, end)]
    area = lst[smallest_ind] * (end - start + 1)
    left_area = _largest_histogram(lst, start, smallest_ind - 1, cache)
    right_area = _largest_histogram(lst, smallest_ind + 1, end, cache)
    return max(area, left_area, right_area)

def find_smallest(lst, start, end):
    smallest_ind = start
    for i in range(start, end + 1):
        if lst[i] < lst[smallest_ind]:
            smallest_ind = i
    return smallest_ind, lst[smallest_ind]

def largest_histogram_2(lst):
    left_smaller = [-1] * len(lst)
    right_smaller = [len(lst)] * len(lst)

    for i in range(1, len(lst)):
        p = i - 1
        while p >= 0 and lst[p] >= lst[i]:
            p = left_smaller[p]
        left_smaller[i] = p

    for i in range(len(lst) - 2, -1, -1):
        p = i + 1
        while p <= len(lst) - 1 and lst[p] >= lst[i]:
            p = right_smaller[p]
        right_smaller[i] = p
    print(left_smaller)
    area = 0
    for i in range(len(lst)):
        area = max(area, (right_smaller[i] - left_smaller[i] - 1) * lst[i])
    return area
print(largest_histogram([2, 1, 5, 6, 2, 3]))


