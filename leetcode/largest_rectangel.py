def largest_rec(lst):
    stack = []
    max_area = 0
    for i in range(len(lst)):
        if not stack or lst[i] >= lst[stack[-1]]:
            stack.append(i)
        else:
            while stack and lst[stack[-1]] > lst[i]:
                last = stack.pop()
                area = lst[last] * (i - last)
                if area > max_area:
                    max_area = area
            stack.append(i)
    if stack:
        last_ind = stack[-1]
    while stack:
        ind = stack.pop()
        if not stack:
            area = lst[ind] * len(lst)
        else:
            area = lst[ind] * (last_ind - ind + 1)
        if area > max_area:
            max_area = area
    return max_area

print(largest_rec([2,1,2]))
