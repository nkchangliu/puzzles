def remove_leftmost(root):
    node, _ = _remove_leftmost(root)
    return node

def _remove_leftmost(root):
    if not root:
        return None, 0
    elif not root.left and not root.right:
        return root, 1
    else:
        left, left_level = _remove_leftmost(root.left)
        right, right_level = _remove_leftmost(root.right)
        if right_level > left_level:
            return right, right_level + 1
        return left, left_level + 1

