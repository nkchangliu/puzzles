# given two string s and t, check if s is a subsequence of t

def is_subsequence(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i+= 1
        j += 1
    return i == len(s)
print(is_subsequence('acvda', 'aacdvsdeaf'))

