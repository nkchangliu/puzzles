def detect_cycle(node):
    slow, fast = node, node
    if not fast or not fast.next:
        return None
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    if not fast or not fast.next:
        return None
    curr = node
    while curr != slow:
        curr = curr.next
        slow = slow.next
    return curr

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
