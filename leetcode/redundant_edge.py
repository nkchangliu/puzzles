def find_redundant(lst):
    roots = {}
    for [pair_s, pair_e] in lst:
        if find(roots, pair_s) == find(roots, pair_e):
            return [pair_s, pair_e]
        else:
            roots = union(roots, pair_s, pair_e)

def find(roots, node):
    if node not in roots:
        return node
    while roots[node] != node:
        roots[node] = roots[roots[node]]
        node = roots[node]
    return node

def union(roots, node1, node2):
    root1, root2 = find(roots, node1), find(roots, node2)
    roots[root1] = root2
    roots[root2] = root2
    return roots

