# given two list return the element that are in both of the list and has smallest sum

def min_index_sum(lst1, lst2):
    index_dict = {}
    for counter, ele in enumerate(lst1):
        index_dict[ele] = counter

    min_index_sum, min_index_ele = None, []
    for i in range(len(lst2)):
        if lst2[i] in index_dict:
            index_sum = i + index_dict[lst2[i]]
            if min_index_sum == None or index_sum < min_index_sum:
                min_index_sum = index_sum
                min_index_ele = [lst2[i]]
            elif index_sum == min_index_sum:
                min_index_ele.append(lst2[i])
    return min_index_ele


print(min_index_sum(["k", "KFC"], ["k", "KFC"]))
