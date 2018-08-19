def candy_swap(a, b):
    exchange = (sum(a) - sum(b))//2
    set_b = set(b)
    for num in a:
        if num - exchange in set_b:
            return [num, num-exchange]
    return [-1, -1]


