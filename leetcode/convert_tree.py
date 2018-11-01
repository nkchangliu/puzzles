class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

from queue import Queue
class CBTInserter:

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.arr = convert_to_arr(root)

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        size = len(self.arr)
        node = TreeNode(v)
        self.arr.append(node)
        print(size)
        print((size - 1) // 2)
        parent = self.arr[(size - 1) //2]
        if size % 2 == 0:
            parent.right = node
        else:
            parent.left = node
        return parent.val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.arr[0]

def convert_to_arr(root):
    arr = []
    q = Queue()
    q.put(root)
    while not q.empty():
        node = q.get()
        arr.append(node)
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)
    return arr

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6


tree = CBTInserter(node1)
for node in tree.arr:
    print(node.val)
print(len(tree.arr))
print(tree.insert(7))
