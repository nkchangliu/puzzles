from queue import Queue
def add_one_row(root, v, d):
    if d == 1:
        new_root = TreeNode(v)
        new_root.left = root
        return new_root
    q = Queue()
    q.put((root, 1))
    while not q.empty():
        node, depth = q.get()
        if depth == d - 1:
            left, right = node.left, node.right
            node.left = TreeNode(v)
            node.right = TreeNode(v)
            node.left.left = left
            node.right.right = right
        else:
            if node.left:
                q.put((node.left, depth + 1))
            if node.right:
                q.put((node.right, depth + 1))
    return root
