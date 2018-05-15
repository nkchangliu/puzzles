def three_sum(lst):
    num_dict = {k : v for v, k in enumerate(lst)}

    res = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            value = 0 - lst[i] - lst[j]
            if value in num_dict and num_dict[value] != i and num_dict[value] != j:
                res.add(tuple(sorted([lst[i], lst[j], value])))

    return list(res)

print(three_sum([-1, 1, 0, 2, -2, 2, -2, 0]))
