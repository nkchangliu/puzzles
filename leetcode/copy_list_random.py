def copy_lst(head):
    if not head:
        return None
    new_head = RandomListNode(head.label)
    old_curr = head
    new_curr = new_head
    while old_curr and old_curr.next:
        new_curr.next = RandomListNode(old_curr.next.label)
        new_curr = new_curr.next
        old_curr = old_curr.next

    old_curr = head
    new_curr = new_head

    while old_curr:
        if old_curr.random:
            ind = find_random(head, old_curr)
            new_curr.random = find_node(new_head, ind)
        new_curr = new_curr.next
        old_curr = old_curr.next
    return new_head

def find_random(head, old_curr):
    rand = head
    count = 0
    while rand and rand != old_curr.random:
        count += 1
        rand = rand.next
    return count

def find_node(head, ind):
    curr = head
    for i in range(ind):
        curr = curr.next
    return curr

class RandomListNode:
    def __init__(self, label, next=None, random=None):
        self.label = label
        self.next = next
        self.random = random

