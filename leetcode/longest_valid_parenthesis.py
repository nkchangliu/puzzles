def longest_valid(s):
    if len(s) < 2:
        return 0
    dp = [0] * len(s)
    if s[0] == "(" and s[1] == ")":
        dp[1] = 2
    max_len = dp[1]
    for i in range(2, len(s)):
        if s[i] == ")" and s[i - 1] == "(":
            if dp[i - 2]:
                dp[i] = dp[i - 2] + 2
            else:
                dp[i] = 2
            max_len = max(max_len, dp[i])
        elif s[i] == ")" and s[i - 1] == ")":
            left = i - dp[i - 1] - 1
            if left >= 0 and s[left] == "(":
                if dp[left - 1]:
                    dp[i] = dp[i - 1] + 2 + dp[left - 1]
                else:
                    dp[i] = dp[i - 1] + 2
                max_len = max(max_len, dp[i])
    return max_len


