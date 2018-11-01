class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def increasingBST(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    start, end =  modify(root)
    return start

def modify(root):
    print(root.val)
    if not root:
        return None, None
    elif not root.left and not root.right:
        print('lo;')
        return root, root
    elif not root.left:
        right_small, right_large = modify(root.right)
        root.right = right_small
        return root, right_large
    elif not root.right:
        left_small, left_large = modify(root.left)
        left_large.right = root
        return left_small, root
    else:
        right_small, right_large = modify(root.right)
        left_small, left_large = modify(root.left)
        left_large.right = root
        root.right = right_small
    return left_small, right_large

root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)
root.right = TreeNode(6)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(7)
root.right.right.right = TreeNode(9)

root, _ = modify(root)
while root:
    print(root.val)
    root = root.right

