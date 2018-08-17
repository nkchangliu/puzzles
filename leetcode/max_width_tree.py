from queue import Queue

def max_width(root):
    if not root: return 0
    q = Queue()
    q.put((root, 0, 0))
    last_level, left_most, max_width= 0, 0, 1
    while not q.empty():
        node, level, pos = q.get()
        if node.left:
            if level + 1 > last_level:
                last_level = level + 1
                left_most = 2 * pos + 1
            q.put((node.left, level + 1, 2 * pos + 1))
            max_width = max(max_width, 2 * pos + 1 - left_most + 1)
        if node.right:
            if level + 1 > last_level:
                last_level = level + 1
                left_most = 2 * pos + 2
            q.put((node.right, level + 1, 2 * pos + 2))
            max_width = max(max_width, 2 * pos + 2 - left_most + 1)

    return max_width

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = Node(1, None, Node(2))
print(max_width(root))


