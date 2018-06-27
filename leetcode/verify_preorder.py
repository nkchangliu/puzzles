def verify_preorder(pre_order):
    stack = []
    s = pre_order.split(",")
    for c in s:
        stack.append(c)
        while len(stack) > 2 and stack[-3] != "#" and stack[-1] == "#" and stack[-2] == "#":
            del stack[-3:]
            stack.append("#")
    return len(stack) == 1 and stack[0] == "#"


def verify_preorder_2(pre_order):
    s = pre_order.split(",")
    diff = 0
    for c in s:
        diff += 1
        if diff > 1:
            return False
        if c != "#":
            diff -= 2
    return diff == 1


print(verify_preorder_2("9,3,4,#,#,1,#,#,2,#,6,#,#"))
