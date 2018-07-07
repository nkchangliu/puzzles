from queue import Queue

def genetic_mutation(start, end, bank):
    need_to_visit = Queue()
    need_to_visit.put((start, 0))

    while need_to_visit.qsize() > 0:
        node, distance = need_to_visit.get()
        if node == end:
            return distance
        for successor in get_successor(node, bank):
            need_to_visit.put((successor, distance + 1))
    return -1

def get_successor(node, bank):
    lst = []
    for mutation in bank:
        if difference(node, mutation):
            lst.append(mutation)
    for mutation in lst:
            bank.remove(mutation)
    return lst

def difference(node, mutation):
    count = 0
    for i in range(len(node)):
        if node[i] != mutation[i]:
            count += 1
        if count > 1:
            return False
    return count == 1

