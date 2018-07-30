class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    if not root:
        return ". "
    else:
        return str(root.val) + " " + serialize(root.left) + serialize(root.right)

def deserialize(data):
    return helper(data.split())

def helper(lst):
    if lst[0] == ".":
        lst.pop(0)
        return None
    else:
        root = TreeNode(int(lst[0]))
        lst.pop(0)
        root.left = helper(lst)
        root.right = helper(lst)
        return root


def print_tree(tree):
    if not tree:
        return "."
    else:
        return str(tree.val) + "{" + print_tree(tree.left) + print_tree(tree.right) + "}"

tree = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))

tree = deserialize(serialize(tree))
print(print_tree(tree))
