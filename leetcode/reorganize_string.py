import collections

def reorganize(s):
    counts = collections.Counter(s)
    sorted_counts = sorted(counts, key = lambda x: -counts[x])
    sorted_s= ''
    for char in sorted_counts:
        sorted_s += char * counts[char]

    if max(counts.values()) > (len(s) + 1) //2:
        return ''
    res = ''
    first_half = sorted_s[0: (len(s) + 1) // 2]
    second_half = sorted_s[(len(s) + 1) //2:]
    print(sorted_s)
    print(first_half)
    print(second_half)
    for i in range(len(second_half)):
        res += first_half[i]
        res += second_half[i]
    if i + 1 < len(first_half):
        res += first_half[i + 1]
    return res

print(reorganize("abbabbaaab"))


