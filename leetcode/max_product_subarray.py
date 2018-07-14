def max_product(lst):
    max_include_pre = lst[0]
    min_include_pre = lst[0]
    largest = lst[0]
    for i in range(1, len(lst)):
        max_include = max(max_include_pre * lst[i], min_include_pre * lst[i], lst[i])
        min_include = min(max_include_pre * lst[i], min_include_pre * lst[i], lst[i])
        largest = max(largest, max_include)
        max_include_pre, min_include_pre = max_include, min_include
    return largest

print(max_product([-1, -2, -9, -6]))
