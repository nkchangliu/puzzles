def solve(m, n, k, start_r, start_c):
    if k == 0:
        return 0
    dp = [[0 for i in range(n)] for j in range(m)]

    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    total_path = 0
    for i in range(m):
        for j in range(n):
            count = 0
            for d_r, d_c in directions:
                new_r, new_c = i + d_r, j + d_c
                if outside(m, n, new_r, new_c):
                    count += 1
            dp[i][j] = count
    total_path += dp[start_r][start_c]
    for _ in range(1, k):
        new_dp = [[0 for i in range(n)] for j in range(m)]

        for i in range(m):
            for j in range(n):
                new_dp[i][j] = get_sum(dp, i, j, directions, m, n)
        dp = new_dp
        total_path += dp[start_r][start_c]

    return total_path

def outside(m, n, r, c):
    return r < 0 or r >= m or c < 0 or c >= n

def get_sum(dp, i, j, directions, m, n):
    count = 0
    for dir_r, dir_c in directions:
        new_r, new_c = i + dir_r, j + dir_c
        if not outside(m, n, new_r, new_c):
            count += dp[new_r][new_c]
    return count


print(solve(1, 3, 3, 0, 1))
