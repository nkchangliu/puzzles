def partition(lst):
    map = {}
    for i in range(len(lst)):
        if lst[i] not in map:
            map[lst[i]] = set()
        map[lst[i]].add(i)

    res = []
    i = j = 0

    while i < len(lst):
        k = i
        while j < len(lst) and k <= j:
            j = max(j, max(map[lst[k]]))
            k += 1
        if j < len(lst):
             res.append(j -i + 1)
        else: res.append(j - i)
        j += 1
        i = k = j
    return res

print(partition("ababcbacadefegdehijhklij"))


