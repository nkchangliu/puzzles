def find_height(root):
    if not root:
        return 0
    else:
        return 1 + max(find_height(root.left), find_height(root.right))

def diameter(root):
    if not root:
        return 0
    else:
        return max(diameter(root.left), diameter(root.right), find_height(root.left) + find_height(root.right))



