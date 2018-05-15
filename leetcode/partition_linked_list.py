# partition a singly linked list based on the num of value, so that small ones comes before large or equal ones

def partition(lst, x):
    curr = lst
    small, small_end, large, large_end = None, None, None, None

    while curr:
        if curr.val < x:
            small, small_end = add_to(curr, small, small_end)
        else:
            large, large_end = add_to(curr, large, large_end)
        curr = curr.next

    if small_end:
        small_end.next = large
    if large_end:
        large_end.next = None

    if small:
        return small
    return large

def add_to(curr, head, end):
    if end:
        end.next = curr
        end = end.next
    else:
        head = curr
        end = head
    return head, end

class Node(object):

    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def test():
    lst = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))
    res = partition(lst, 3)
    while res:
        print(res.val)
        res = res.next

test()
