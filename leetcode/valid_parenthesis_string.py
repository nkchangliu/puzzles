def valid_string(s):
    open = set()
    open.add(0)
    for c in s:
        if not open or max(open) < 0:
            return False
        elif c == "(":
            open = update(open, 1)
        elif c == ")":
            open = update(open, -1)
        else:
            open = update(open, 1) |  update(open, -1) | open
    return 0 in open

def update(open, num):
    new_open = set()
    for ele in open:
        if ele + num >= 0:
            new_open.add(ele + num)
    return new_open


print(valid_string("(())((())()()(*)(*()(())())())()()((()())((()))(*"))
