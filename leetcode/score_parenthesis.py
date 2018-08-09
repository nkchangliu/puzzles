def score_parenthesis(s):
    open = total = 0
    for i in range(len(s)):
        if s[i] == "(":
            open += 1
        else:
            open -= 1
            if s[i - 1] == "(":
                total += 2 ** open
    return total

print(score_parenthesis("(()())()"))
