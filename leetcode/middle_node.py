def middle_node(head):
    curr = head
    count = 0
    while curr:
        count += 1
        curr = curr.next

    mid = count // 2
    curr = head
    for i in range(mid):
        curr = curr.next

    return curr.val

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))

print(middle_node(head))
