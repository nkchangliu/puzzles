def knight_off_board(N, k, r, c):
    directions = [(1, 2), (2, 1), (-1, 2), (1, - 2), (-2, 1), (2, -1), (-1, -2), (-2, -1)]
    dp = [[1 for i in range(N)] for j in range(N)]
    for _ in range(k):
        new_dp = [[1 for i in range(N)] for j in range(N)]
        for i in range(N):
            for j in range(N):
                new_dp[i][j] = calculate(directions, i, j, dp, N)
        dp = new_dp
        print(dp)
    return dp[r][c]

def calculate(directions, i, j, dp, N):
    prob = 0
    for dir_r, dir_c in directions:
        new_r, new_c = i + dir_r, j + dir_c
        if new_r >= 0 and new_r < N and new_c >= 0 and new_c < N:
            prob += 1/8 * dp[new_r][new_c]
    return prob

print(knight_off_board(3, 2, 0, 0))
