def reorder(head):
    if not head or not head.next:
        return head
    curr_odd = head
    even_head = head.next
    curr_even = head.next
    while curr_odd and curr_even and curr_even.next and curr_even.next.next:
        curr_odd.next = curr_even.next
        curr_odd = curr_odd.next
        curr_even.next = curr_odd.next
        curr_even = curr_even.next
    if curr_even.next:
        curr_odd.next = curr_even.next
        curr_even.next = None
        curr_odd = curr_odd.next
    curr_odd.next = even_head
    return head

class ListNode(object):
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
