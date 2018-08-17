def basic_calculator(s):
    lst = []
    i = 0
    for j in range(len(s)):
        if not s[j].isdigit() and s[j] != " ":
            lst.append(int(s[i : j]))
            lst.append(s[j])
            i = j + 1
    lst.append(int(s[i : ]))

    new_lst = []
    i = 0
    while i < len(lst):
        if lst[i] != "*" and lst[i] != "/":
            new_lst.append(lst[i])
            i += 1
        else:
            if lst[i] == "*":
                num = new_lst.pop()
                num *= lst[i + 1]
                new_lst.append(num)
            if lst[i] == "/":
                num = new_lst.pop()
                num //= lst[i + 1]
                new_lst.append(num)
            i += 2

    res = new_lst[0]
    i = 1
    while i < len(new_lst):
        if new_lst[i] == "+":
            res += new_lst[i + 1]
        elif new_lst[i] == "-":
            res -= new_lst[i + 1]
        i += 2
    return res

print(basic_calculator("3+22*2/2-3"))

