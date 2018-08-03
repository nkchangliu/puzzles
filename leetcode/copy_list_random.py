def copy_lst(head):
    if not head:
        return None
    cache = {}
    new_head = RandomListNode(head.label)
    old_curr = head
    new_curr = new_head
    cache[old_curr] = new_curr
    while old_curr and old_curr.next:
        new_curr.next = RandomListNode(old_curr.next.label)
        new_curr = new_curr.next
        old_curr = old_curr.next
        cache[old_curr] = new_curr

    old_curr = head
    while old_curr:
        if old_curr.random:
            cache[old_curr].random = cache[old_curr.random]
        old_curr = old_curr.next
    return new_head

class RandomListNode:
    def __init__(self, label, next=None, random=None):
        self.label = label
        self.next = next
        self.random = random

