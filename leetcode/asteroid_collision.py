def asteroid_collision(lst):
    stack = []
    i = 0
    while i < len(lst):
        while stack and i < len(lst) and is_collision(stack[-1], lst[i]):
            if abs(stack[-1]) < abs(lst[i]):
                stack.pop()
            elif abs(stack[-1]) == abs(lst[i]):
                stack.pop()
                i += 1
            else:
                i += 1
        if i < len(lst):
            stack.append(lst[i])
            i += 1
    return stack

def is_collision(a, b):
    if a > 0 and b < 0:
        return True

print(asteroid_collision([10, 8, -5, -11]))
