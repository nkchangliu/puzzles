from queue import Queue

def zig_zag(root):
    if not root:
        return []
    q = Queue()
    q.put((root, 0))
    res, sub_res  = [], []
    old_level = None
    while not q.empty():
        node, level = q.get()

        if old_level != level:
            if sub_res:
                res.append(sub_res)
            sub_res = [node.val]
        else:
            sub_res.append(node.val)
        old_level = level

        if node.left:
            q.put((node.left, level + 1))
        if node.right:
            q.put((node.right, level + 1))
    res.append(sub_res)

    for i in range(1, len(res), 2):
        res[i] = res[i][::-1]
    return res

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))

print(zig_zag(root))
