def product_array(lst):
    if not lst:
        return []
    res = []
    product = 1
    for num in lst:
        res.append(product)
        product *= num

    product = 1
    for i in range(len(lst) - 1, -1, -1):
        res[i] = res[i] * product
        product *= lst[i]

    return res

print(product_array([1, 2, 3, 4]))

