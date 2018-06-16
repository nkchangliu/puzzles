def beautiful(num):
    visited = [False] * (num + 1)
    count = 0
    count = calculate(num, 1, visited, count)
    return count

def calculate(num, pos, visited, count):
    if pos > num:
        count += 1
    for i in range(1, num + 1):
        if not visited[i] and (pos % i == 0 or i % pos == 0):
            visited[i] = True
            count = calculate(num, pos + 1, visited, count)
            visited[i] = False
    return count

print(beautiful(2))
