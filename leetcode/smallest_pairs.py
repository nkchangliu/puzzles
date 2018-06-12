import heapq

def smallest_pairs(nums1, nums2, k):
    if not nums1 or not nums2:
        return []

    pq = []
    visited = set()
    heapq.heappush(pq, (nums1[0] + nums2[0], (0, 0)))
    res = []
    while len(res) < k and pq:
        val, (i, j) = heapq.heappop(pq)
        res.append([nums1[i], nums2[j]])
        if i + 1 < len(nums1) and (i + 1, j) not in visited:
            visited.add((i + 1, j))
            heapq.heappush(pq, (nums1[i + 1] + nums2[j], (i + 1, j)))
        if j + 1 < len(nums2) and (i, j + 1) not in visited:
            visited.add((i, j + 1))
            heapq.heappush(pq, (nums1[i] + nums2[j + 1], (i, j + 1)))
    return res

print(smallest_pairs([1, 7, 11], [2, 3, 6], 4))

