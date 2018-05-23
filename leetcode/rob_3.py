def rob(root):
    cache = {}
    return max_robber(root, cache)

def max_robber(root, cache):
    if root not in cache:
        if root == None:
            res =  0
        elif root.left == None and root.right == None:
            res = root.val
        else:
            with_root = root.val + with_out_robber(root.left, cache) + with_out_robber(root.right, cache)
            without_root = max_robber(root.left, cache) + max_robber(root.right, cache)
            res = max(with_root, without_root)
        cache[root] = res
    return cache[root]

def with_out_robber(root, cache):
    if not root:
        return 0
    return max_robber(root.left, cache) + max_robber(root.right, cache)

class TreeNode(object):
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


tree = TreeNode(3, TreeNode(5, TreeNode(4), TreeNode(5)))
print(rob(tree))

