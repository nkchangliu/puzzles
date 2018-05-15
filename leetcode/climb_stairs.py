def climb_stairs(n):
    climb_count = {}
    climb_count[1] = 1
    climb_count[2] = 2
    for i in range(3, n+1):
        climb_count[i] = climb_count[i - 1] + climb_count[i - 2]
    return climb_count[n]

print(climb_stairs(3))
