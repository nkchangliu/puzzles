from collections import Counter

def sort_str(s):
    table = Counter(s)
    lst = sorted([(x, table[x]) for x in table], key = lambda x: x[1], reverse = True)
    res = ""
    for c, count in lst:
        res += c * count
    return res

print(sort_str('tree'))
