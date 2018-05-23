def get_intersection_node(headA, headB):
    a_len = get_length(headA)
    b_len = get_length(headB)

    if a_len > b_len:
        long_head = headA
        short_head = headB
    else:
        long_head = headB
        short_head = headA

    for i in range(abs(a_len - b_len)):
        long_head = long_head.next

    while long_head and short_head:

        if long_head == short_head:
            return long_head
        long_head = long_head.next
        short_head = short_head.next

    return None


def get_length(head):
    curr = head
    count = 0
    while curr:
        count += 1
        curr = curr.next
    return count


class Node(object):
    def __init__(self, val, next = None):
        self.val = val
        self.next = next


headA = Node(3)
headB= Node(1, headA)

