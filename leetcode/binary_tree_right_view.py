def right_view(root):
    ans = compute(root, [], 0)
    return ans

def compute(root, ans, level):
    if root:
        if len(ans) == level:
            ans.append(root.val)

        compute(root.right, ans, level + 1)
        compute(root.left, ans, level + 1)

