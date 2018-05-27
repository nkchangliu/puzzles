def course_schedule(lst):
    prereq = {}
    for start, end in lst:
        if end not in prereq:
            prereq[end] = set()
        if start not in prereq:
            prereq[start] = set()
        prereq[end].add(start)

    to_do, prereq = get_to_do([], prereq)

    while to_do:

        node = to_do.pop()
        prereq = remove_pre(prereq, node)

        to_do, prereq = get_to_do(to_do, prereq)

    return len(prereq) == 0

def remove_pre(prereq, node):
    for key in prereq:
        if node in prereq[key]:
            prereq[key].remove(node)
    return prereq

def get_to_do(to_do, prereq):
    for key in prereq:
        if len(prereq[key]) == 0:
            to_do.append(key)
    for node in to_do:
        if node in prereq:
            prereq.pop(node)
    return to_do, prereq

print(course_schedule([[1, 0], [2, 0]]))
