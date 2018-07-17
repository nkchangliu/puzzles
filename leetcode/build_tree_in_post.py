def build_tree(inorder, postorder):
    if not inorder:
        return None
    root = TreeNode(postorder[-1])
    for i in range(len(inorder)):
        if inorder[i] == postorder[-1]:
            break
    root.left = build_tree(inorder[0:i], postorder[0:i])
    root.right = build_tree(inorder[i+1:], postorder[i:-1])
    return root


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
