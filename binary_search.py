def binary_search(element, some_list):
    start = 0
    end = len(some_list)
    while True:
        mid = (start + end) // 2
        if element == some_list[mid]:
            return mid
        elif element < some_list[mid]:
            end = mid
        elif element > some_list[mid]:
            start = mid
        if mid == 0 or mid == len(some_list)-1:
            break
    return None

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))

"""
# 해설
def binary_search(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1

    while start_index <= end_index:
        midpoint = (start_index + end_index) // 2
        if some_list[midpoint] == element:
            return midpoint
        elif some_list[midpoint] > element:
            end_index = midpoint - 1
        else:
            start_index = midpoint + 1
    return None
"""
