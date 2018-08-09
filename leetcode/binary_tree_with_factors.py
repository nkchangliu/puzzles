def binary_tree_factors(lst):
    lst.sort()
    res = {}
    for i in range(len(lst)):
        num = lst[i]
        count = 1
        for j in range(i):
            if num % lst[j] == 0 and num // lst[j] in res:
                count += res[lst[j]] * res[num // lst[j]]
        res[num] = count

    total = 0
    for key in res:
        total += res[key]

    print(res)

    return total % (10 ** 9 + 7)

print(binary_tree_factors([2, 4, 5, 10]))
