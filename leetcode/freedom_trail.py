def freedom_trail(rings, keys):
    index_dict = {}
    for i in range(len(rings)):
        ring = rings[i]
        if ring not in index_dict:
            index_dict[ring] = []
        index_dict[ring].append(i)

    cache = [(0, 0)]
    for s in keys:
        locations = index_dict[s]
        cache = update_cache(cache, locations, len(rings))
    return min([x[1] for x in cache])

def update_cache(cache, locations, length):
    new_cache = []
    for location in locations:
        new_cache.append(find_best(cache, location, length))
    return new_cache

def find_best(cache, location, length):
    min_distance = float("inf")
    for i in range(len(cache)):
        distance = get_distance(cache[i][0], location, length) + cache[i][1]
        if distance < min_distance:
            min_distance = distance
    return location, min_distance + 1

def get_distance(ind1, ind2, length):
    return min(abs(ind1 - ind2), length - abs(ind1 - ind2))


