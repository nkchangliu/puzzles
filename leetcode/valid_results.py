def calculate(s):
    lst = []
    i = 0
    while i < len(s):
        if not s[i].isdigit():
            lst.append(s[i])
            i += 1
        else:
            j = i
            while j < len(s) and s[j].isdigit():
                j += 1
            lst.append(int(s[i: j]))
            i = j
    return _solve(lst, 0, len(lst) - 1)

def _solve(lst, lo, hi):
    if lo == hi:
        return [lst[lo]]
    res = []
    for i in range(lo, hi):
        if not str(lst[i]).isdigit():
            left = _solve(lst, lo, i - 1)
            right = _solve(lst, i+1, hi)
            res += combine(left, right, lst[i])
    return res

def combine(left, right, operator):
    res = []
    for num1 in left:
        for num2 in right:
            res.append(apply(num1, num2, operator))
    return res

def apply(num1, num2, op):
    if op == "*": return num1 * num2
    if op == "-": return num1 - num2
    if op == "+": return num1 + num2
    if op == "/": return num1 / num2

print(calculate("2*3-4*5"))


