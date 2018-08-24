def traversal(matrix):
    m = len(matrix)
    n = len(matrix[0])
    directions =  [(-1, 1), (1, -1)]
    dir = 0
    curr = (0, 0)
    res = []
    while len(res) < m * n:
        while with_in_range(curr, m, n):
            res.append(matrix[curr[0]][curr[1]])
            curr = curr[0] + directions[dir][0], curr[1] + directions[dir][1]
        curr = reset(curr, m, n)
        dir = 1- dir
        print(res)
    return res

def with_in_range(curr, m, n):
    return curr[0] >=0 and curr[0] < m and curr[1] >= 0 and curr[1] < n

def reset(curr, m, n):
    print(curr)
    if curr[0] == -1 and curr[1] == n:
        return 1, n - 1
    if curr[0] == m and curr[1] == -1:
        return m - 1, 1
    if curr[0] == -1:
        return 0, curr[1]
    if curr[0] == m :
        return m-1, curr[1] + 2
    if curr[1] == -1:
        return curr[0], 0
    if curr[1] == n :
        return curr[0] + 2, n - 1

print(traversal([[1, 2, 3], [4, 5, 6,], [7, 8, 9], [10, 11, 12]]))

