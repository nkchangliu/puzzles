from queue import Queue
def snakes_ladders(board):
    q = Queue()
    q.put((1, 0))
    visited = set()
    visited.add(1)
    while not q.empty():
        node, level = q.get()
        print(node, level)
        if node == len(board) ** 2:
            return level
        for successor in get_successor(board, node):
            if successor not in visited:
                visited.add(successor)
                q.put((successor, level + 1))
    return -1

def get_successor(board, node):
    res = []
    for i in range(1, 7):
        successor = node + i
        r, c = get_row_col(board, successor)
        if r is not None and c is not None and board[r][c] == -1:
            res.append(successor)
        elif r is not None and c is not None:
            res.append(board[r][c])
    return res

def get_row_col(board, num):
    n = len(board) # 4
    r = (num - 1) // n # 4 // 4 = 1
    if r % 2 != 0:
        c = n -1 - (num-1) % n # c = 4 - 4 % 4 = 4
    else:
        c = (num - 1) % n
    r = n - 1 - r
    if 0<=r<n and 0<=c<n:
        return r, c
    return None, None

board =[
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,35,-1,-1,13,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,15,-1,-1,-1,-1]]

for i in range(1, 17):
    print(get_row_col(board, i))
print(snakes_ladders(board))
