def common_ancestor(root, node1, node2):
    ancestors = get_ancestors(root)
    ancestors_node1 = set()
    while node1 != ancestors[node1]:
        ancestors_node1.add(node1)
        node1 = ancestors[node1]
    ancestors.node1.add(node1)
    while node2 not in ancestors_node1:
        node2 = ancestors[node2]
    return node2

def get_ancestors(root):
    ancestors = {}
    ancestors[root] = root
    stack = [root]
    while stack:
        node = stack.pop()
        if node.left:
            ancestors[node.left] = node
            stack.append(node.left)
        if node.right:
            ancestors[node.right] = node
            stack.append(node.right)
    return ancestors


def common_ancestor_recursive(root, node1, node2):
    if not root or root == node1 or root == node2:
        return root
    left = common_ancestor_recursive(root.left, node1, node2)
    right = common_ancestor_recursive(root.right, node1, node2)
    if left and right:
        return root
    return left if left else right

