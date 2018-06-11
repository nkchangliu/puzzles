def find_n_fib(n):
    cache = {}
    cache[0] = 0
    cache[1] = 1
    for i in range(2, n):
        cache[i] = cache[i -1] + cache[i -2]
    return cache[n - 1]

def find_n_fib_2(n):
    x = 0
    y = 1
    for _ in range(2, n):
        x, y = y, x+ y
    return y

print(find_n_fib_2(10))
