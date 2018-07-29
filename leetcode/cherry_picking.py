def cherry_picking(grid):
    n = len(grid)
    dp = [[-float("inf") for i in range(n)] for j in range(n)]
    dp[0][0] = grid[0][0]
    for t in range(1, 2 * n - 1):
        new_dp = [[-float("inf") for i in range(n)] for j in range(n)]
        for i in range(max(0, t - (n - 1)), min(n - 1, t) + 1):
            for j in range(max(0, t - (n - 1)), min(n - 1, t) + 1):
                if grid[i][t - i] != -1 and grid[j][t - j] != -1:
                    val = grid[i][t - i]
                    if j != i:
                        val += grid[j][t - j]
                    new_dp[i][j] = val + max(dp[pi][pj] for pi in (i - 1, i) for pj in (j - 1, j) if pi >=0 and pj >= 0)
        print(new_dp)
        dp = new_dp
    return max(0, dp[-1][-1])


grid = [[1, 1, -1], [1, -1, 1], [-1, 1,  1]]
print(cherry_picking(grid))
