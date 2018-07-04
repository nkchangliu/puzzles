def fib_array(s):
    for i in range(1, min(10, len(s))):
        first = s[:i]
        if first != "0" and first.startswith("0"):
            break
        for j in range(i + 1, min(i + 10, len(s))):
            second = s[i:j]
            if second != "0" and second.startswith("0"):
                break
            fib = calculate(s, i, j)
            if len(fib) >= 3:
                return fib
    return []

def calculate(s, i, j):
    fib = [int(s[:i]), int(s[i:j])]
    start = j
    while start < len(s):
        next_num = fib[-1] + fib[-2]
        next_s = str(next_num)
        if (next_s[0] == "0" or not next_s.startswith("0")) and s[start :].startswith(next_s) and next_num <= 2**31 -1:
            fib.append(next_num)
            start += len(next_s)
        else:
            return []
    return fib

print(fib_array("11235813"))


