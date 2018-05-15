def count_n_say(n):
    start = "1"
    for i in range(n - 1):
        start = count_n_say_helper(start)
    return start


def count_n_say_helper(string):
    lst = list(string)
    res = []
    i, j = 0, 0
    while i < len(lst) and j < len(lst):
        if lst[i] == lst[j]:
            j += 1
        else:
            res.append(str(j - i))
            res.append(lst[i])
            i = j
    res.append(str(j - i))
    res.append(lst[i])
    return ''.join(res)

print(count_n_say(4))
