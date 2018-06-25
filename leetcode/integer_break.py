def integer_break(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    lst = [1] * (n + 1)
    lst[2], lst[3] = 2, 3
    for i in range(4, n + 1):
        lst[i] = max(lst[left] * lst[i - left] for left in range(n // 2 + 1))
    return lst[n]

print(integer_break(10))
