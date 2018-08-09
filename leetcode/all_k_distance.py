from queue import Queue
def all_k_distance(root, target, distance):
    prev = {}
    calculate_prev(root, prev)

    visited = set()
    visited.add(target)
    q = Queue()
    q.put((target, 0))
    res = []
    while not q.empty():
        node, d = q.get()
        if d == distance:
            res.append(node.val)
        if d > distance:
            break
        for successor in get_successor(prev, node):
            if successor not in visited:
                q.put((successor, d + 1))
                visited.add(successor)
    return res

def get_successor(prev, node):
    res = []
    if node in prev:
        res.append(prev[node])
    if node.left:
        res.append(node.left)
    if node.right:
        res.append(node.right)
    return res

def calculate_prev(root, prev):
    if root:
        if root.left:
            prev[root.left] = root
            calculate_prev(root.left, prev)
        if root.right:
            prev[root.right] = root
            calculate_prev(root.right, prev)

