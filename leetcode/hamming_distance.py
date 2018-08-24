def hamming_distance(lst):
    res = {}
    for num in lst:
        i = 0
        while num > 0:
            if num % 2 == 1:
	        res[i] = 1 if i not in res else res[i] + 1
            num = num // 2
            i += 1
    dis = 0
    for key in res:
        dis += res[key] * (len(lst) - res[key])
    return dis

print(hamming_distance([4, 14, 2]))

