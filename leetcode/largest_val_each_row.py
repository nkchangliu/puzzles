from queue import Queue
def largest_val_each_row(root):
    if not root:
        return []
    q = Queue()
    q.put(root)
    q.put('eor')
    res = []
    max_val = -float('inf')
    while q.qsize() > 0:
        next_node = q.get()
        if next_node != 'eor':
            if next_node.left is not None:
                q.put(next_node.left)
            if next_node.right is not None:
                q.put(next_node.right)
            max_val = max(max_val, next_node.val)
        else:
            res.append(max_val)
            max_val = -float('inf')
            if q.qsize() > 0:
                q.put('eor')
    return res

def largest_val(root):
    queue = [root]
    res = []
    max_val = -float('inf')

    while queue:
        new_queue = []
        for node in queue:
            max_val = max(max_val, node.val)
            if node.left is not None:
                new_queue.append(node.left)
            if node.right is not None:
                new_queue.append(node.right)
        queue = new_queue
        res.append(max_val)
        max_val = -float('inf')
    return res

class TreeNode:
     def __init__(self, x, left = None, right = None):
         self.val = x
         self.left = left
         self.right = right

tree = TreeNode(1, TreeNode(3, TreeNode(5),TreeNode(3)),TreeNode(2, None, TreeNode(9)))

print(largest_val(tree))

