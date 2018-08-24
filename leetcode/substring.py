def count_substring(lst):
    map = {}
    longest = 0
    for i in range(len(lst)):
        if i != 0 and is_adj(lst[i - 1], lst[i]):
             longest += 1
        else:
             longest = 1
        map[lst[i]] = max(longest, map[lst[i]] if lst[i] in map else 0)
    return sum(map.values())

def is_adj(c1, c2):
    return ord(c2) - ord(c1) == 1 or ord(c1) - ord(c2) == 25

