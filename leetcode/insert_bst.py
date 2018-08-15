def insert_tree(root, target):
    if not root:
        root = TreeNode(target)
    elif root.val > target:
        root.left = insert_tree(root.left, target)
    else:
        root.right = insert_tree(root.right, target)
    return root

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
