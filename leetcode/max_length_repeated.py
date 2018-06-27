def max_length_repeat(A, B):
    ans = [[0 for i in range(len(B))] for j in range(len(A))]
    for i in range(len(A)):
        if A[i] == B[0]:
            ans[i][0] = 1
    for j in range(len(B)):
        if B[j] == A[0]:
            ans[0][j] = 1
    for i in range(1, len(A)):
        for j in range(1, len(B)):
            ans[i][j] = ans[i - 1][j - 1] + 1 if A[i] == B[j] else 0
    return max(ans[i][j] for i in range(len(A)) for j in range(len(B)))
print(max_length_repeat([0,0,0,0,1], [1, 0, 0, 0, 0]))
