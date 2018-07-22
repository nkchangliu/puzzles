def path_sum(root, sum):
    return [x[::-1] for x in  helper(root, sum)]

def helper(root, sum):
    if not root:
        return []
    if root and not root.left and not root.right and root.val == sum:
        return [[root.val]]
    elif root and not root.left and not root.right:
        return []
    else:
        left_lst = helper(root.left, sum - root.val)
        right_lst = helper(root.right, sum - root.val)
        new_lst = left_lst + right_lst
        for lst in new_lst:
            lst.append(root.val)
        return new_lst

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

