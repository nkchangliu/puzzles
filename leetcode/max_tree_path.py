def max_path_sum(root):
    _, max_sum = _max_path_sum(root)
    return max_sum

def _max_path_sum(root):
    if not root.left and not root.right:
        return root.val, root.val
    elif not root.right:
        sub_path_left, max_path_left = _max_path_sum(root.left)
        return max(sub_path_left + root.val, root.val), max(root.val + sub_path_left, max_path_left, root.val)
    elif not root.left:
        sub_path_right, max_path_right = _max_path_sum(root.right)
        return max(sub_path_right + root.val, root.val), max(root.val + sub_path_right, max_path_right, root.val)

    sub_path_left, max_path_left = _max_path_sum(root.left)
    sub_path_right, max_path_right = _max_path_sum(root.right)
    max_path = max(max_path_left, max_path_right, root.val + max(0, sub_path_left, sub_path_right, sub_path_left + sub_path_right))
    return root.val + max(0, sub_path_left, sub_path_right), max_path


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

tree = Node(-10, Node(9), Node(20, Node(15), Node(7)))

print(max_path_sum(tree))
