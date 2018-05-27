def build_tree(preorder, inorder):
    if not preorder:
        return None
    elif len(preorder) == 1:
        return TreeNode(preorder[0])

    root = TreeNode(preorder[0])
    ind = inorder.index(preorder[0])
    inorder_left = inorder[0:ind]
    inorder_right = inorder[ind+1:]
    preorder_left = preorder[1:ind+1]
    preorder_right = preorder[ind+1:]
    print(inorder_left)
    print(inorder_right)
    print(preorder_left)
    print(preorder_right)
    root.left = build_tree(preorder_left, inorder_left)
    root.right = build_tree(preorder_right, inorder_right)

    return root
class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
build_tree([3, 9, 20, 15], [9, 3, 15, 20])
