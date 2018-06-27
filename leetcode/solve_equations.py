def solve_equations(equations, results, queries):
    adjacency_list, nodes = get_adjacency_list(equations, results)
    values = generate_values(adjacency_list, nodes)
    print(values)
    res = solve_queries(values, queries)
    return res

def get_adjacency_list(equations, results):
    adjacency_list = {}
    nodes = set()
    for i in range(len(equations)):
        first, second = equations[i][0], equations[i][1]
        nodes.add(first)
        nodes.add(second)
        if first not in adjacency_list:
            adjacency_list[first] = set()
        adjacency_list[first].add((second, results[i]))
        if second not in adjacency_list:
            adjacency_list[second] = set()
        adjacency_list[second].add((first, 1/ results[i]))
    return adjacency_list, nodes

def generate_values(adjacency_list, nodes):
    values = {}
    need_to_visit = []
    while nodes:
        start = nodes.pop()
        values[start] = (1, start)
        need_to_visit.append(start)

        while need_to_visit:
            node = need_to_visit.pop()
            if node in nodes:
                nodes.remove(node)
            for successor, res in adjacency_list[node]:
                if successor not in values and successor not in need_to_visit:
                    values[successor] = (values[node][0] / res, start)
                    need_to_visit.append(successor)
    return values

def solve_queries(values, queries):
    res = []
    for query in queries:
        if query[0] in values and query[1] in values and values[query[0]][1] == values[query[1]][1]:
            res.append(values[query[0]][0] / values[query[1]][0])
        else:
            res.append(-1.0)

    return res

equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
print(solve_equations([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))
