from queue import Queue

def bus_route(lsts, start, end):
    if start == end:
        return 0
    graph, stops_graph, start_buses = make_graph(lsts, start)
    q = Queue()
    visited = set()
    for start_bus in start_buses:
        q.put((start_bus, 1))
    visited.add(start_bus)

    while q.qsize() > 0:
        bus, depth = q.get()
        if end in stops_graph[bus]:
            return depth
        for successor in graph[bus]:
            if successor not in visited:
                visited.add(successor)
                q.put((successor, depth + 1))
    return -1

def make_graph(lsts, start):
    graph = {}
    start_buses = []
    stops_graph = {}

    for bus_num, bus_stops in enumerate(lsts):
        stops_graph[bus_num] = set(bus_stops)

    for i in range(len(lsts)):
        graph[i] = set()
        for j in range(len(lsts)):
            if i != j and bool(stops_graph[i] & stops_graph[j]):
                graph[i].add(j)

    for i in range(len(lsts)):
        if start in stops_graph[i]:
            start_buses.append(i)
    return graph, stops_graph, start_buses


print(make_graph([[1, 2, 3], [3, 6, 7]], 1))

print(bus_route([[1, 2, 7], [3, 6, 7]], 1, 3))
