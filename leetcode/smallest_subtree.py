def smallest_subtree(root):
    node, _ = helper(root)
    return node

def helper(root):
    if not root:
        return root, 0

    left_node, left_depth = helper(root.left)
    right_node, right_depth = helper(root.right)

    if left_depth > right_depth:
        return left_node, left_depth + 1
    elif left_depth < right_depth:
        return right_node, right_depth + 1

    return root, left_depth + 1


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
print(smallest_subtree(root))
