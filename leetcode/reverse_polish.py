def reverse_polish(lst):
    stack = []
    for c in lst:
        if c.isdigit() or c[1:].isdigit():
            stack.append(int(c))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(calculate(num1, num2, c))
        print(stack)
    return stack[0]

def calculate(num1, num2, c):
    if c == "+":
        return num1 + num2
    if c == "/":
        return divide(num1, num2)
    if c == "*":
        return num1 * num2
    if c == "-":
        return num1 - num2

def divide(num1, num2):
    val = abs(num1) // abs(num2)
    if num1 * num2 < 0:
        return -val
    return val


print(reverse_polish(["4","-2","/","2","-3","-","-"]))
