def triangle(lst):
    if not lst:
        return 0
    memory = [i for i in lst[-1]]
    for i in range(len(lst) - 2, -1, -1):
        new_mem = [num for num in lst[i]]
        for j in range(len(lst[i])):
            new_mem[j] += min(memory[j], memory[j + 1])
        memory = new_mem

    return memory[0]

