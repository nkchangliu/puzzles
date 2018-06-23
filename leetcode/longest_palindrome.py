import collections

def longest_palindrome(s):
    res = 0
    for v in collections.Counter(s).values():
        res += v //2 * 2
        if res % 2 == 0 and v % 2 != 0:
            res += 1
    return res

print(longest_palindrome('abccccdd'))
