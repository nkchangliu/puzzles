def daily_temp(temps):
    cache = {}
    res = []
    for i in range(len(temps) - 1, -1, -1):
        cache[temps[i]], ind = i, float('inf')
        for value in range(temps[i] + 1, 101):
            if value in cache:
                ind = min(ind, cache[value])
        if ind == float('inf'):
            res.append(0)
        else:
            res.append(ind - i)
    return list(reversed(res))

def daily_temp_2(temps):
    res, stack = [], []
    for i in range(len(temps) - 1, -1, -1):
        while stack and temps[stack[-1]] <= temps[i]:
            stack.pop()
        if not stack:
            res.append(0)
        else:
            res.append(stack[-1] - i)
        stack.append(i)
    return list(reversed(res))


print(daily_temp_2([73, 74, 75, 71, 69, 72, 76, 73]))
