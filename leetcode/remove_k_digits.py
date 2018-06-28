
def remove_k_digits(num, k):
    stack = []
    for digit in num:
        while stack and stack[-1] > digit and k > 0:
            stack.pop()
            k -= 1
        stack.append(digit)
    while k > 0:
        stack.pop()
        k -= 1
    return str(int(''.join(stack))) if stack else '0'

print(remove_k_digits('120892', 2))


