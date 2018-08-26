def last_number(n):
    i, left,step, remaining = 1, 1, 1, n
    while remaining > 1:
        if left or remaining % 2:
            i += step
        left = 1 - left
        step *= 2
        remaining //= 2
    return i

print(last_number(9))

