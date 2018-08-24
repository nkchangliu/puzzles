def match_making(lst):
    count = sum(lst)
    if count % 4 != 0: return False
    return solve(lst, [count // 4] * 4, 0)


def solve(lst, targets, index):
    if index == len(lst):
        return True
    for i in range(0, 4):
        if targets[i] < lst[index]: continue
        targets[i] -= lst[index]
        if solve(lst, targets, index + 1): return True
        targets[i] += lst[index]
    return False
