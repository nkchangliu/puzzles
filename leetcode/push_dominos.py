def push_dominos(s):
    lst = list(s)
    symbols = [(i, symbol) for i, symbol in enumerate(lst) if symbol != '.']
    symbols = [(-1, 'L')] + symbols + [(len(lst), 'R')]
    for i in range(len(symbols) - 1):
        start_i, start_symbol = symbols[i]
        end_i, end_symbol = symbols[i + 1]
        if start_symbol == end_symbol:
            for x in range(start_i + 1, end_i):
                lst[x] = end_symbol
        elif start_symbol == "R" and end_symbol == "L":
            for x in range(start_i + 1, start_i + (end_i - start_i + 1) //2):
                lst[x] = "R"
            for x in range(end_i, end_i - (end_i - start_i + 1) // 2, -1):
                lst[x] = "L"
    return ''.join(lst)

print(push_dominos(".L.R...LR..L.."))

