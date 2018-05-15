def largest_palindrome(n):
    num = 10 ** n
    lst = []
    for i in reversed(range(num//10, num)):
        palin = create_palindrome(i)
        if can_be_dividen(palin, num):
            return palin % 1337

    return 9

def can_be_dividen(palin, num):
    for i in reversed(range(num//10, num)):
        if palin % i == 0 and palin / i < num:
            return True
        if palin / i > i:
            return False
    return False


def create_palindrome(left):
    num = left
    right = 0
    while num > 0:
        left *= 10
        right = right * 10 + num % 10
        num = num // 10
    return left + right

for i in range(1, 9):
    print(largest_palindrome(i))
