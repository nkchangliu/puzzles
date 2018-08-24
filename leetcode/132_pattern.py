def pattern(lst):
    smallest = float("inf")
    left_min = [smallest]
    for num in lst:
        smallest = min(num, smallest)
        left_min.append(smallest)
    stack = []
    for i in range(len(lst) - 1, 0, -1):
        if lst[i] > left_min[i]:
             while stack and stack[-1] <= left_min[i]:
                 stack.pop()
             if stack and stack[-1] < lst[i]:
                 return True
        stack.append(lst[i])
    return False

print(pattern([1, 0, 1, -4, -3]))

