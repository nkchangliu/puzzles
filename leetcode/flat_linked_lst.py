def flat(root):
    root, _ = _flat(root)
    return root

def _flat(root):
    node = root
    while node and node.next and not node.child:
        node = node.next
    if not node or not node.child:
        return root, node
    next_start, next_end = _flat(node.next)
    child_start, child_end = _flat(node.child)
    node.child = None
    node.next, child_start.prev = child_start, node
    if next_start:
        child_end.next, next_start.prev = next_start, child_end
    return root, next_end

