def monotone_increasing(num):
    num_lst = [int(n) for n in str(num)]
    stack = [num_lst[0]]

    for i in range(1, len(num_lst)):
        last_num  = num_lst[i]
        if not stack or last_num >= stack[-1]:
            stack.append(last_num)
        else:
            count = 0
            while stack and stack[-1] >= last_num:
                last_num = stack.pop()
                count += 1
            stack.append(last_num - 1)
            stack.append("9" * (len(num_lst) + count - i - 1))
            return int("".join(str(n) for n in stack))
    return num

print(monotone_increasing(4356))
print(monotone_increasing(3534))
print(monotone_increasing(1234))
