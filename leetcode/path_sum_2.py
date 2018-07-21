def path_sum(root, sum):
    res = []
    helper(root, sum, [], res)
    return res

def helper(root, sum, path, res):
    if root and root.left is None and root.right is None and root.val = sum:
        path.append(root.val)
        res.append(path)
    elif root is not None:
        left_path = path + [root.val]
        right_path = path + [root.val]
        helper(root.left, sum - root.val, left_path, res)
        helper(root.right, sum - root.val, right_path, res)

