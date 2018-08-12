def uncommon_word(a, b):
    lst_a = a.split()
    lst_b = b.split()
    map = {}
    for ele in lst_a:
        if ele in map:
            map[ele] += 1
        else:
            map[ele] = 1
    for ele in lst_b:
        if ele in map:
            map[ele] += 1
        else:
            map[ele] = 1
    return [ele for ele in map if map[ele] == 1]

print(uncommon_word("this apple is sweet", "this apple is sour"))
