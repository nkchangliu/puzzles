# reverse a linked list iteratively and recursively

def reverse_list(head):
    if not head or not head.next:
        return head
    first, second = head, head.next
    first.next = None
    while first and second and second.next:
        curr = second.next
        second.next = first
        second, first = curr, second
    second.next = first
    return second

def reverse_recursive(head):
    if not head or not head.next:
        return head
    new_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head



class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next




