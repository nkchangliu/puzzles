def split_array(lst):
    dict = {}
    for num in lst:
        dict[num] = 1 if num not in dict else dict[num] + 1
    prev, p1, p2, p3 = -float("inf"), 0, 0, 0
    for num in sorted(dict.keys()):
        if num - 1 > prev:
            if p1 + p2 > 0:
                return False
            else:
                p1 = dict[num]
        elif num - 1 == prev:
            if p1 + p2 > dict[num]:
                return False
            else:
                p3, p2, p1 = p2 + min(p3, dict[num] - p1 - p2), p1, max(0, dict[num] - p1 - p2 - p3)
        prev = num
    return p1 + p2 <= 0

print(split_array([1, 2, 3,3, 4, 4, 5]))
