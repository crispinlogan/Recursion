"""
From https://www.youtube.com/watch?v=IJDJ0kBx2LM at ~49mins in
there is merge sort, but this is quick sort (I just did it anyway)
"""

def quick_sort(arr):
    """
    This works by defining a pivot, which can be, for example, the first element
    in the array (it can actually be any element), and then we make a left array
    with element smaller than pivot, and a right array with elements larger than
    pivot. We then call the quick_sort recursively with the left and right array
    (see func below). We do this until we have 0 or 1 element in the array passed
    to quick_sort recursively and in that case return the array passed to quick_sort
    """
    # base case
    if len(arr) <= 1:
        return arr
    # recursive case
    pivot = arr[0]
    left_arr = [el for el in arr[1:] if el < pivot]
    right_arr = [el for el in arr[1:] if el > pivot]
    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)

def test_quick_sort():
    assert quick_sort([2,1,3]) == [1,2,3]
    assert quick_sort([1,4,99,-8,3]) == [-8,1,3,4,99]
    assert quick_sort([1]) == [1]
    assert quick_sort([]) == []
