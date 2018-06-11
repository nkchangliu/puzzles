def symmetric_tree(root):
    if not root:
        return True
    return is_mirror(root.left, root.right)

def is_mirror(root1, root2):
    if not root1 and not root2:
        return True
    elif not root1 or not root2:
        return False
    else:
        return root1.val == root2.val and \
                is_mirror(root1.left, root2.right) and is_mirror(root1.right, root2.left)
