def solve(root):
    if not root:
        return 0
    stack, total = [], 0
    stack.append((root, root.val))
    while stack:
        node, val = stack.pop()
        if not node.left and not node.right:
            total += val
        else:
            if node.left:
                stack.append((node.left, 10 * val + node.left.val))
            if node.right:
                stack.append((node.right, 10 * val + node.right.val))
     return total

