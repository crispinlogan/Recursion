def mergeSort(arr):
    # base case
    if len(arr) == 0:
        return []
    # recursive case
    pivot = arr[len(arr)//2]
    left_arr = [element for element in arr if element < pivot]
    right_arr = [element for element in arr if element > pivot]
    pivot_arr = [element for element in arr if element == pivot]
    return mergeSort(left_arr) + pivot_arr + mergeSort(right_arr)


mergeSort([5,3,7,2,9,8]) # [2, 3, 5, 7, 8, 9]
mergeSort([5,3,7,2,9,8, 7]) # [2, 3, 5, 7, 7, 8, 9]

# to see speed differences
mergeSort(list(range(1000000,-1,-1)))
(list(range(1000000,-1,-1))).sort()
# check outputs are same
mergeSort(list(range(1000000,-1,-1))) == sorted(list(range(1000000,-1,-1)))
