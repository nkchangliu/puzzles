def three_sum_no_set(lst):
    lst = sorted(lst)
    res = []
    for i in range(len(lst) - 2):
        if (i == 0 or lst[i] != lst[i - 1]):
            target = 0 - lst[i]
            lo, hi = i + 1, len(lst) - 1
            while lo < hi:
                if lst[lo] + lst[hi] == target:
                    res.append([lst[i], lst[lo], lst[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and lst[lo] == lst[lo - 1]:
                        lo += 1
                    while lo < hi and lst[hi] == lst[hi + 1]:
                        hi -= 1
                elif lst[lo] + lst[hi] > target:
                    hi -= 1
                else:
                    lo += 1
    return res

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
print(three_sum_no_set([-1, 1, 0, 2, -2, 2, -2, 0]))
