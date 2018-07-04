def max_binary_tree(lst):
    if not lst:
        return None
    max_ind = lst.index(max(lst))
    root = TreeNode(lst[max_ind])
    root.left = max_binary_tree(lst[0: max_ind])
    root.right = max_binary_tree(lst[max_ind + 1:])
    return root

