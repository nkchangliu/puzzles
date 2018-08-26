def solve(n):
    if n == 0:
        return [None]
    if n == 1:
        return [TreeNode(0)]
    res = []
    for i in range(n):
        if i % 2 == 1 and (n - i - 1) % 2 == 1:
            left = solve(i)
            right = solve(n - i - 1)
            for i in range(len(left)):
                for j in range(len(right)):
                    root = TreeNode(0)
                    root.left = left[i]
                    root.right = right[j]
                    res.append(root)
    return res

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


