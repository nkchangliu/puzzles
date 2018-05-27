
'''
[1, 2, 4, 4, 7]
[1, 3, 4, 1, 3]

'''

def smallest_back(front, back):
    all_num = set()
    dup_num = set()
    for i in range(len(front)):
        all_num.add(front[i])
        all_num.add(back[i])
        if front[i] == back[i]:
            dup_num.add(front[i])
    non_dup = all_num.difference(dup_num)
    return min(non_dup) if len(non_dup) != 0 else 0

print(smallest_back([1, 2, 4, 4, 7], [1, 3, 4, 1, 3]))
