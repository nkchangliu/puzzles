def duplicate_subtree(root):
    res = []
    counts = {}
    serialize(root, res, counts)
    return res


def serialize(root, res, counts):
    if root is None:
        return "#"
    else:
        serial = str(root.val)
        serial += serialize(root.left, res, counts)
        serial += serialize(root.right, res, counts)
    counts[serial] = 1 if serial not in counts else counts[serial] + 1

    if counts[serial] == 2:
        res.append(root)
    return serial
