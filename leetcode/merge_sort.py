# merge sort a linked list

def merge_sort(lst):
    if not lst or lst.next:
        return lst
    elif not lst.next.next:
        if lst.val > lst.next.val:
            lst.next.next = lst
            lst = lst.next
            lst.next.next = None
        return lst

    middle_node = find_middle(lst)
    first = lst
    second = middle_node.next
    middle_node.next = None

    first_front = merge_sort(first)
    second_front = merge_sort(second)

    return merge(first_front, second_front)


def find_middle(lst):
    length = 0
    curr = lst
    while curr:
        length += 1
        curr = curr.next
    curr = lst
    for i in range(length // 2 - 1):
        curr = curr.next
    return curr

def merge(first, second):
    curr1 = first
    curr2 = second
    start = Node(0)
    curr = start
    while curr1 and curr2:
        if curr1.val < curr2.val:
            curr.next = curr1
            curr1 = curr1.next
        else:
            curr.next = curr2
            curr2 = curr2.next
        curr = curr.next
    if curr1:
        curr.next = curr1
    else:
        curr.next = curr2
    return start.next

class Node(object):
    def __init__(self, val, next = None):
        self.val =val
        self.next = next



