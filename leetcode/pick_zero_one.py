def pick(lst, m, n):
    return pick_str(lst, 0, m, n, {})

def pick_str(lst, start, m, n, cache):
    if start == len(lst) or (m == n == 0):
        return 0
    if (start, m, n) in cache:
        return cache[(start, m, n)]
    not_include = pick_str(lst, start + 1, m, n, cache)
    include = 0
    ones, zeros = count_one_zero(lst[start])
    if ones <= n and zeros <= m:
        include = 1 + pick_str(lst, start + 1, m - zeros, n- ones, cache)
    cache[(start, m, n)] = max(include, not_include)
    return cache[(start, m,n)]

def count_one_zero(s):
    ones = zeros = 0
    for c in s:
        if c == "0":
            zeros += 1
        else:
            ones += 1
    return ones, zeros

def DP_pick(lst, m, n):
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for s in lst:
        ones, zeros = count_one_zero(s)
        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                dp[i][j] = max(dp[i][j], 1 + dp[i - zeros][j - ones] if i - zeros >= 0 and j -ones >=0 else 0)
        print(dp)
    return dp[m][n]

print(DP_pick(["10", "1", "0"], 1, 1))
