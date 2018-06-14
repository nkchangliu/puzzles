
def next_num(num):
    digits = [int(i) for i in str(num)]
    i = len(digits) - 1
    while i > 0 and digits[i] <= digits[i - 1]:
        i -= 1
    if i == 0:
        return -1
    replace = i - 1
    smallest = i
    for j in range(i, len(digits)):
        if digits[j] > digits[replace] and digits[j] < digits[smallest]:
            smallest = j
    digits[smallest], digits[replace] = digits[replace], digits[smallest]
    res = digits[0:i] + sorted(digits[i:])
    n = int(''.join(map(str, res)))
    return n if n < 2**31 else -1
print(next_num(123432))
