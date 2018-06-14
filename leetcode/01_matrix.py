from queue import Queue

def make_matrix(matrix):
    q = Queue()
    row = len(matrix)
    col = len(matrix[0])
    res = [[None for i in range(col)] for j in range(row)]

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                q.put((i, j))

    while not q.empty():
        i, j = q.get()
        if matrix[i][j] == 0:
            res[i][j] = 0
        for successor_i, successor_j in valid_successor(i, j, res):
            q.put((successor_i, successor_j))
            if res[successor_i][successor_j] is None or res[successor_i][successor_j] > res[i][j] + 1:
                res[successor_i][successor_j] = res[i][j] + 1
    return res

def valid_successor(i, j, res):
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    successors = []
    for row, col in directions:
        new_i, new_j = i + row, col + j
        if new_i >= 0 and new_i < len(res) and new_j >= 0 and new_j < len(res[0]) \
                and res[new_i][new_j] is None:
            successors.append((new_i, new_j))
    return successors

def DP_solve(matrix):
    row = len(matrix)
    col = len(matrix[0])
    res = [[float("inf") for i in range(col)] for j in range(row)]
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                res[i][j] = 0
    for i in range(row):
        for j in range(col):
            min_val = res[i][j]
            if i-1 >= 0 and res[i - 1][j] + 1 < min_val:
                min_val = res[i - 1][j] + 1
            if j-1 >= 0 and res[i][j - 1] + 1 < min_val:
                min_val = res[i][j - 1] + 1
            res[i][j] = min_val

    for i in range(row-1, -1, -1):
        for j in range(col-1, -1, -1):
            min_val = res[i][j]
            if i+1 < row and res[i + 1][j] + 1 < min_val:
                min_val = res[i + 1][j] + 1
            if j+1 < col and res[i][j + 1] + 1 < min_val:
                min_val = res[i][j + 1] + 1
            res[i][j] = min_val
    return res

print(valid_successor(1, 0, [[0, 0, 0],[0, None, None], [None, None, None]]))
print(DP_solve([[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]]))

