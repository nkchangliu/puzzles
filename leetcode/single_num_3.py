def single_num(lst):
    s = set()
    for num in lst:
        if num not in s:
            s.add(num)
        else:
            s.remove(num)
    return list(s)
