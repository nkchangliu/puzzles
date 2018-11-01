def total_fruit(tree):
    s = e = 0
    types = {}
    length = 0
    while e < len(tree):
        while e < len(tree) and len(types) <= 2:
            fruit = tree[e]
            types[fruit] = 1 if fruit not in types else types[fruit] + 1
            e += 1
        if e == len(tree) and len(types) <= 2:
            length = max(length, e - s)
        else:
            length = max(length, e - s - 1)
        print(length)
        while len(types) > 2:
            fruit = tree[s]
            types[fruit] -= 1
            if types[fruit] == 0:
                del types[fruit]
            s += 1
    return length

print(total_fruit([3,3,3,1,2,1,1,2,3,3,4]))
