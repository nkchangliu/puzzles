def find_str(lst):
    res = set()
    for s in lst:
        res.add(even_odd_s(s))
    return len(res)

def even_odd_s(s):
    even = {}
    odd = {}
    for i in range(len(s)):
        if i % 2 == 0:
            even[s[i]] = even[s[i]] + 1 if s[i] in even else 1
        else:
             odd[s[i]] = odd[s[i]] + 1 if s[i] in odd else 1
    res = ''
    keys = sorted(odd)
    for key in keys:
        res= res + key + str(odd[key])

    keys = sorted(even)
    for key in keys:
        res = res +  key + str(even[key])
    return res

print(find_str(["abc","acb","bac","bca","cab","cba"]))
