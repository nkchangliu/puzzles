def number_islands(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                count += 1
                update(matrix, i, j)
    return count

def update(matrix, i, j):
    matrix[i][j] = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dir_r, dir_c in directions:
        new_r, new_c = dir_r + i, dir_c + j
        if inside(matrix, new_r, new_c) and matrix[new_r][new_c] == 1:
            update(matrix, new_r, new_c)

def inside(matrix, r, c):
    return r >= 0 and r < len(matrix) and c >= 0 and c < len(matrix[0])

print(number_islands([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]]))
