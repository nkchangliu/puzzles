def all_path(graph):
    paths = get_path(graph, 0, len(graph) - 1)
    return [x[::-1] for x in paths]

def get_path(graph, s, e):
    if s == e:
        return [[s]]
    sub_path = []
    for node in graph[s]:
        sub_path += get_path(graph, node, e)
    return [x + [s] for x in sub_path]


print(all_path([[1,2], [3], [3], []]))
