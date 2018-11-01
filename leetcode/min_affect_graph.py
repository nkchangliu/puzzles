import collections
def min_malware_node(graph, initial):
    initial.sort()
    visited = set()
    initial_affected = collections.defaultdict(set)
    for node in initial:
        print(node)
        if node not in visited:
            visited.add(node)
            affect_nodes(node, graph, visited, initial_affected)
    return max(initial_affected.keys(), key=lambda x: len(initial_affected[x]), default=initial[0])


def affect_nodes(node, graph, visited, initial_affected):
    stack = [node]
    while stack:
        curr = stack.pop()
        for next_node, connect in enumerate(graph[curr]):
            if connect and next_node not in visited:
                visited.add(next_node)
                stack.append(next_node)
                initial_affected[node].add(next_node)


print(min_malware_node(graph, initial))
