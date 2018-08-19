def build_tree(pre, post):
    if not pre:
        return None
    if len(pre) == 1:
        return TreeNode(pre[0])
    root = TreeNode(pre[0])
    for i in range(len(pre)):
        if post[i] == pre[1]:
            break
    root.left = build_tree(pre[1: i+2], post[0: i + 1])
    root.right = build_tree(pre[i+2: ], post[i + 1: -1])
    return root

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.righ = right


