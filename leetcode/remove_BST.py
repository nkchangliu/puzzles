def delete_node(root, target):
    if not root:
        return root
    if root.val == target:
        if not root.left and not root.right: return None
        elif not root.left: return root.right
        elif not root.right: return root.left
        else:
            return move_left_right(root.left, root.right)
    if root.val < target:
        root.right = delete_node(root.right, target)
    else:
        root.left = delete_node(root.left, target)
    return root


def move_left_right(left, right):
    root = right
    while root and root.left:
         root = root.left
    root.left = left
    return right



class Node:
    def __init__(self, val, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

root = Node(5, Node(3, Node(2), Node(4)), Node(6, None, Node(7)))
root = delete_node(root, 3)


def print_tree(root):
    if not root:
       print("None")
    elif root:
       print(root.val)
       print_tree(root.left)
       print_tree(root.right)

print_tree(root)
