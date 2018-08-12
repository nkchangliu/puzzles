def dislike_group(n, dislikes):
    nodes, graph = make_graph(dislikes)
    print(graph)
    stack = []
    map = {}
    while nodes or stack:
        if not stack:
            node = nodes.pop()
            stack.append(node)
            map[node] = 0
        while stack:
            print(map)
            node = stack.pop()
            for successor in graph[node]:
                if successor in map and map[successor] == map[node]:
                    return False
                elif successor not in map:
                    map[successor] = 1 - map[node]
                    stack.append(successor)
                    nodes.remove(successor)
    return True

def make_graph(dislikes):
    nodes = set()
    graph = {}
    for start, end in dislikes:
        nodes.add(start)
        nodes.add(end)
        if start not in graph:
            graph[start] = set()
        graph[start].add(end)
        if end not in graph:
            graph[end] = set()
        graph[end].add(start)
    return nodes, graph

