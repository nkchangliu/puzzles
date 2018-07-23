def post_order(root):
    if not root:
        return []
    lst1 = post_order(root.left)
    lst2 = post_order(root.right)
    return lst1 + lst2 + [root.val]


class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = Node(1, None, Node(2, Node(3)))
print(post_order(root))
