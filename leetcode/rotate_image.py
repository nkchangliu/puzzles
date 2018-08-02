def rotate(matrix):
    row = len(matrix)
    col = len(matrix[0])

    for i in range(row):
        for j in range(col // 2):
            matrix[i][j], matrix[i][col - 1 - j] = matrix[i][col - 1 - j], matrix[i][j]
    for i in range(row - 1, -1, -1):
        for j in range(col - i - 1):
            print(matrix[i][j])
            matrix[i][j], matrix[row - 1 - j][col - 1 - i] = matrix[row - 1 - j][col - 1 - i], matrix[i][j]

    return matrix

input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate(input))

