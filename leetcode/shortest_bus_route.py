from queue import Queue

def bus_route(lsts, start, end):
    graph = make_graph(lsts)
    q = Queue()
    visited = set()
    q.put((start, 0))
    visited.add(start)

    while q.qsize() > 0:
        node, depth = q.get()
        for successor in graph[node]:
            if successor == end:
                return depth + 1
            if successor not in visited:
                visited.add(successor)
                q.put((successor, depth + 1))
    return -1

def make_graph(lsts):
    graph = {}
    for lst in lsts:
        for num in lst:
            if num not in graph:
                graph[num] = set(lst)
            else:
                graph[num].update(set(lst))
    return graph




print(bus_route([[1, 2, 7], [3, 6, 7]], 1, 3))
