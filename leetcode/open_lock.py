from queue import Queue
def open_lock(deadends, target):
    start = "0000"
    deadends = set(deadends)
    q = Queue()
    visited = set()
    if start not in deadends:
        q.put((start, 0))
        visited.add(start)
    while not q.empty():
        node, dist = q.get()
        if node == target:
            return dist
        for successor in get_successor(node):
            if successor not in deadends and successor not in visited:
                q.put((successor, dist + 1))
                visited.add(successor)
    return -1

def get_successor(node):
    old_node = list(node)
    new_nodes = []
    for i in range(4):
        new_nodes += get_new(old_node, i)
    return new_nodes

def get_new(old_node, i):
    node1 = old_node[0:i]
    node2 = old_node[0:i]
    digit = old_node[i]
    if digit == "0":
        node1.append("9")
        node2.append("1")
    else:
        node1.append(str((int(digit) + 1) % 10))
        node2.append(str((int(digit) - 1) % 10))
    node1 += old_node[i + 1:]
    node2 += old_node[i + 1:]
    return  ["".join(node1)] + ["".join(node2)]

print(open_lock(["0201","0101","0102","1212","2002"], "0202"))




