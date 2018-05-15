def rotate_list(head, k):
    if not head:
        return head

    curr = head
    length = 1
    while curr != None and curr.next != None:
        curr = curr.next
        length += 1

    curr.next = head
    step = k % length

    for i in range(length - step):
        curr = curr.next
    head = curr.next
    curr.next = None

    return head

class Node(object):

    def __init__(self, value, next = None):
        self.value = value
        self.next = next


def test():
    head = Node(1, Node(2, Node(3, Node(4))))
    head = rotate_list(head, 1)
    while head != None:
        print(head.value)
        head = head.next

test()
