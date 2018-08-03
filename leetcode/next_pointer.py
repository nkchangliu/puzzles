END = "end_here"
from queue import Queue
def next_pointer(node):
    if not node:
        return None
    open = Queue()
    open.put(node)
    open.put(END)

    old_node = None
    while not open.empty():
        next_node = open.get()
        if next_node == END:
            if not open.empty():
                open.put(END)
                old_node = open.get()
                if old_node.left:
                    open.put(old_node.left)
                if old_node.right:
                    open.put(old_node.right)
        else:
            if next_node.left:
                open.put(next_node.left)
            if next_node.right:
                open.put(next_node.right)
            if old_node:
                old_node.next = next_node
            old_node = next_node


