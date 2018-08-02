def generate_parentheses(num):
    if num == 0:
        return []
    res = [[""]]
    for i in range(1, num + 1):
        sub_res = []
        for ind in range(i):
            sub_res += ["(" + x + ")" + y for x in res[ind] for y in res[i - ind - 1]]
        print(res)
        res.append(sub_res)
    return res[-1]

print(generate_parentheses(3))

