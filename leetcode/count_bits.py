def count_bits(num):
    res = [0, 1, 1, 2]
    if num <= 3:
        return res[0: num + 1]
    while len(res) <= num:
        res += [1 + x for x in res]
    return res[0: num + 1]

print(count_bits(16))
