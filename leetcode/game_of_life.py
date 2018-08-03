ALIVE = 2
DEAD = -2

def game_of_life(matrix):
    row = len(matrix)
    col = len(matrix[0])

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0 and turn_alive(matrix, i, j):
                matrix[i][j] = ALIVE

            if matrix[i][j] == 1 and turn_dead(matrix, i, j):
                matrix[i][j] = DEAD

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == ALIVE:
                matrix[i][j] = 1
            if matrix[i][j] == DEAD:
                matrix[i][j] = 0
    return matrix


def alive_count(matrix, i, j):
    directions = [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if not (x == 0 and y == 0)]
    count = 0
    for dir_r, dir_c in directions:
        new_r, new_c = i + dir_r, j + dir_c
        if inside(matrix, new_r, new_c) and (matrix[new_r][new_c] == 1 or matrix[new_r][new_c] == DEAD):
                count += 1
    return count

def inside(matrix, r, c):
    return r >= 0 and r < len(matrix) and c >= 0 and c <len(matrix[0])

def turn_alive(matrix, i, j):
    return matrix[i][j] == 0 and alive_count(matrix, i, j) == 3

def turn_dead(matrix, i, j):
    count = alive_count(matrix, i, j)
    return matrix[i][j] == 1 and (count < 2 or count > 3)


print(game_of_life([ [0,1,0], [0,0,1],[1,1,1],[0,0,0]]))
