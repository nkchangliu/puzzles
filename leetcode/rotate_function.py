def rotate_function(lst):
    if len(lst) < 2:
        return 0
    total = sum(lst)
    function = sum(i * lst[i] for i in range(len(lst)))
    max_f = function

    for i in range(len(lst) - 1):
        new_function = function - (total - lst[i]) + (len(lst) - 1) * lst[i]
        max_f = max(max_f, new_function)
        function = new_function


    return max_f

print(rotate_function([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
