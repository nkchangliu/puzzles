def bipartite(graph):
    stack = []
    map = {}
    need_to_visit = set([x for x in range(len(graph))])
    while stack or need_to_visit:
        if not stack:
            node = need_to_visit.pop()
            stack.append(node)
            map[node] = 0
        node = stack.pop()
        for successor in graph[node]:
            if successor in map and map[successor] == map[node]:
                return False
            elif successor not in map:
                map[successor] = 1 if map[node] == 0 else 0
                stack.append(successor)
                need_to_visit.remove(successor)
    return True
print(bipartite([[1,3], [0,2], [1,3], [0,2]]))
