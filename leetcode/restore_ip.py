def restore_ip(s):
    lst = restore(s,4)
    return ['.'.join(inner) for inner in [x[::-1] for x in lst]]

def restore(s, n):
    if not s and n == 0:
        return [[]]
    elif not s or n < 0:
        return []
    first = s[0]
    lst1 = calculate(first, restore(s[1:], n - 1))
    lst2, lst3 = [], []
    if len(s) > 1 and not s[0:2].startswith('0'):
        lst2 = calculate(s[0:2], restore(s[2:], n - 1))
    if len(s) > 2 and not s[0:3].startswith('0') and int(s[0:3]) < 256:
        lst3 = calculate(s[0:3], restore(s[3:], n - 1))
    return lst1 + lst2 + lst3

def calculate(pre, lsts):
    for lst in lsts:
        lst.append(pre)
    return lsts


print(restore_ip("25525511135"))
