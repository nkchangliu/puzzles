def spiral_matrix(n):
    matrix = [[0 for i in range(n)] for j in range(n)]
    return spiral(matrix, 0, 1, n)

def spiral(matrix, start, num, n):
    if num > n ** 2:
        return matrix

    for i in range(start, n - start):
        matrix[start][i] = num
        num += 1
    for j in range(start + 1, n - start - 1):
        matrix[j][n - start - 1] = num
        num += 1
    for i in reversed(range(start, n - start)):
        if matrix[n - start - 1][i] == 0:
            matrix[n - start - 1][i] = num
            num += 1
    for j in reversed(range(start + 1, n - start - 1)):
        if matrix[j][start] == 0:
            matrix[j][start] = num
            num += 1
    return spiral(matrix, start + 1, num, n)

for i in range(6):
    print(spiral_matrix(i))
