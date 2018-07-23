def reverse_k_group(root, k):
    count = 0
    curr = root
    while curr and count < k:
        curr = curr.next
        count += 1
    if count < k:
        return root
    sub_head = reverse_k_group(curr, k)
    new_head, tail = reverse(root, k)
    tail.next = sub_head
    return new_head

def reverse(start, k):
    if k == 1 or not start:
        return start, start
    if start:
        new_start, new_end = reverse(start.next, k - 1 )
        new_end.next = start
        start.next = None
    return new_start, start

class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

root = Node(1, Node(2, Node(3, Node(4, Node(5)))))
root = reverse_k_group(root, 2)
while root:
    print(root.val)
    root = root.next

