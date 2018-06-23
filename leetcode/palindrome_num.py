def palindrome_num(num):
    s = str(num)
    for i in range(len(s) //2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True


def palindrome_num2(num):
    if num < 0 or (num % 10 == 0 and num != 0):
        return False
    reversed_num = 0
    while num > reversed_num:
        reversed_num = reversed_num * 10 + num % 10
        num = num // 10
    return num == reversed_num or num == reversed_num // 10

print(palindrome_num2(10))
