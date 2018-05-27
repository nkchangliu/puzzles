def decode(s):
    stack, curr_string, num = [], '', 0
    for c in s:
        if c == "[":
            stack.append(curr_string)
            stack.append(num)
            curr_string = ''
            num = 0
        elif c == "]":
            count = stack.pop()
            print(count)
            prev_string = stack.pop()
            print(prev_string)
            print(curr_string)
            curr_string = prev_string + count * curr_string
        elif c.isdigit():
            num = num * 10 + int(c)
        else:
            curr_string += c

    return curr_string


