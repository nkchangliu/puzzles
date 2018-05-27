def unique(n):
    tree = {}
    tree[0] = 1
    tree[1] = 1
    for i in range(2, n + 1):
        tree[i] = 0
        for j in range(0, i):
            tree[i] += tree[j] * tree[i - j - 1]
    return tree[n]

print(unique(3))
