def friends_circle(lst):
    count = len(lst)
    heads = list(range(len(lst)))
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i][j] == 1:
                hi, hj = find(heads, i), find(heads, j)
                if hi != hj:
                    heads[hi] = hj
                    count -= 1
    return count

def find(heads, i):
    while heads[i] != i:
        heads[i] = heads[heads[i]]
        i = heads[i]
    return heads[i]
