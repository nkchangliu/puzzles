import heapq
def smallest_range(nums):
    q = [(x[0],i, 0) for i, x in enumerate(nums)]
    heapq.heapify(q)
    min_res = float("inf")
    while q:
        ele, nums_ind, lst_ind = heapq.heappop(q) 
        if q:
            ele2, nums_ind_2, lst_ind_2 = heapq.heappop(q)
            heapq.heappush(q, (ele2, nums_ind_2, lst_ind_2))
        if ele2 and ele2 - ele < min_res:
            min_res = ele2 - ele
        if lst_ind < len(nums[nums_ind]) - 1:
            heapq.heappush(q, (nums[nums_ind][lst_ind + 1],nums_ind, lst_ind+1) )
    return min_res

nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
print(smallest_range(nums))
