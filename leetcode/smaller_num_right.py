def smaller_num(lst):
    if not lst:
        return []
    res = []
    root = TreeNode(lst[len(lst) - 1], 1)
    res.append(0)
    for i in range(len(lst) - 2, -1, -1):
        num = lst[i]
        count = insert(root, num, 0)
        res.append(count)
    return res[::-1]

def insert(root, num, count):
    if num <= root.val:
        root.count += 1
        if not root.left:
            root.left = TreeNode(num, 1)
        else:
            count = insert(root.left, num, count)
    if num > root.val:
        count += root.count
        if not root.right:
            root.right = TreeNode(num, 1)
        else:
            count = insert(root.right, num, count)
    return count


class TreeNode:
    def __init__(self, val, count=1, left=None, right=None):
        self.val = val
        self.count = count
        self.left = left
        self.right = right


print(smaller_num([1, 0, 2]))

