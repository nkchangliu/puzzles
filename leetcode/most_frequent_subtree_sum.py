def most_frequent(root):
    if not root:
        return []
    cache = {}
    sum_tree(root, cache)
    freq = max(cache.values())
    return [x for x in cache if cache[x] == freq]

def sum_tree(root, cache):
    if not root:
        return 0
    elif not root.left and not root.right:
        cache[root.val] = 1 if root.val not in cache else cache[root.val] + 1
        return root.val
    else:
        left = sum_tree(root.left, cache)
        right = sum_tree(root.right, cache)
        val = left + right + root.val
        cache[val] = 1 if val not in cache else cache[val] + 1
        return val
