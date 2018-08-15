def split_list(node, k):
    curr =  node
    length = 0
    while curr:
        curr = curr.next
        length += 1
    base = length // k
    leftover = length - base * k
    res = []
    curr = node
    res.append(curr)
    for i in range(leftover):
        curr =  _helper(curr, base + 1)
        res.append(curr)
    for i in range(k - leftover - 1):
        curr = _helper(curr, base)
        res.append(curr)
    return res

def _helper(node, length):
    if length == 0:
        return None
    curr =  node
    for i in range(length - 1):
        curr = curr.next
    next_head = curr.next
    curr.next = None
    return next_head

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
