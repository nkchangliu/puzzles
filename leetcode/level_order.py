from queue import Queue
END = "end_level"
def level_order(root):
    if not root:
        return []
    q = Queue()
    q.put(root)
    q.put(END)
    res, sub_res = [], []
    while not q.empty():
        node = q.get()
        if node == END:
            res.append(sub_res)
            sub_res = []
            if not q.empty():
                q.put(END)
        elif node:
            sub_res.append(node.val)
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
    return res

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node = Node(3, Node(9), Node(20, Node(15), Node(7)))
print(level_order(node))
