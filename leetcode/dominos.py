def dominos(n):
    if n <= 1:
        return 1
    res = [1] * (n + 1)
    up = [0] * (n + 1)
    for i in range(2, n):
        res[i] = res[i - 1] + res[i - 2] + 2 * up[i - 1]
        up[i] = up[i - 1] + res[i - 2]
    return res[n]
