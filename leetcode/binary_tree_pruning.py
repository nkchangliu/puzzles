def binary_tree_pruning(root):
    if not root:
        return root
    root.left = binary_tree_pruning(root.left)
    root.right = binary_tree_pruning(root.right)
    if not root.left and not root.right and root.val == 0:
        return None
    else:
        return root

