def palindrome_partition(s):
    cache = palindrome_substring(s)
    result = solve(s, 0, cache)
    return result

def palindrome_substring(s):
    cache = [[i == j  for i in range(len(s))] for j in range(len(s))]

    for i in range(len(s)-1, -1, -1):
        for j in range(i + 1, len(s)):
            if i + 1 == j and s[i] == s[j]:
                cache[i][j] = True
            elif s[i] == s[j] and cache[i+1][j-1]:
                cache[i][j] = True
    return cache

def solve(s, start, cache):
    if start == len(s):
        return [[]]
    palindromes_ind = is_palindrome(start, cache)
    result = []
    for palindrome_ind in palindromes_ind:
        sub_results = solve(s, palindrome_ind + 1, cache)
        for sub_result in sub_results:
            new_sub_result = []
            new_sub_result.append(s[start : palindrome_ind + 1])
            new_sub_result += sub_result
            result.append(new_sub_result)
    return result

def is_palindrome(start, cache):
    return [i for i in range(len(cache)) if cache[start][i]]

print(palindrome_partition('abab'))
