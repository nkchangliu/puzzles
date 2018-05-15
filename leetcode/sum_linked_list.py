def sum_two_list(l1, l2):
    s1, s2, s3 =[], [], []
    curr = l1
    while curr:
        s1.append(curr.value)
        curr = curr.next
    curr = l2
    while curr:
        s2.append(curr.value)
        curr = curr.next

    carryover = 0
    while s1 and s2:
        num = s1.pop() + s2.pop() + carryover
        s3.append(num % 10)
        carryover = num // 10

    while s1:
        num = s1.pop() + carryover
        s3.append(num % 10)
        carryover = num // 10

    while s2:
        num = s2.pop() + carryover
        s3.append(num % 10)
        carryover = num // 10

    if carryover:
        s3.append(carryover)

    l3 = Node(s3.pop())
    curr = l3
    while s3:
        curr.next = Node(s3.pop())
        curr = curr.next

    return l3




class Node(object):
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


def test():
    l1 = Node(7, Node(2, Node(4, Node(3))))
    l2 = Node(5, Node(6, Node(4)))

    l3 = sum_two_list(l1, l2)

    while l3:
        print(l3.value)
        l3 = l3.next

test()
