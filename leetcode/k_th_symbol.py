def k_th_symbol(n, k):
    if n == 1 and k == 1:
        return 0
    if k <= 2 ** ( n - 2):
        return k_th_symbol(n - 1, k)
    else:
        return 1 - k_th_symbol(n - 1, k - 2 ** (n - 2))


