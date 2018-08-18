def next_great(lst):
    if not lst:
        return []
    ind = lst.index(max(lst))
    res, stack = [None] * len(lst), []
    res[ind] = -1
    stack.append(lst[ind])
    for j in range(ind-1, -1, -1):
        update(lst, stack, j, res)
    for j in range(len(lst) - 1, ind, -1):
        update(lst, stack, j, res)
    return res

def update(lst, stack, j, res):
    while stack and stack[-1] <= lst[j]:
        stack.pop()
    if not stack:
        res[j] = -1
    else:
        res[j] = stack[-1]
    stack.append(lst[j])

print(next_great([1, 2, 1]))

