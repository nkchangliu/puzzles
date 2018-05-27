def inorder(root):
    stack = []
    res = []
    curr = root
    while curr or lst:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right

    return res
