def solve(s):
    return delete_one(s, 0, len(s) - 1)

def delete_one(s, start, end):
    if start >= end:
        return True
    while start < end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            break
    return check_palindrome(s, start + 1, end) or check_palindrome(s, start, end -1)

def check_palindrome(s, start, end):
    if start >= end:
        return True
    while start < end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            return False
    return True

print(solve("abca"))
