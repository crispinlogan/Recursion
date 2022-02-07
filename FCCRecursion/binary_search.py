"""
From https://www.youtube.com/watch?v=IJDJ0kBx2LM at ~35mins in
They do a slightly different implementation, but it comes to the same thing
"""

def binary_search(arr, num):
    # base case
    if len(arr) == 1:
        if arr[0] == num:
            return True
        return False
    if len(arr) == 0:
        return False
    # recursive case
    mid = len(arr) // 2
    if arr[mid] == num:
        return True
    if arr[mid] < num:
        return binary_search(arr[mid:], num)
    return binary_search(arr[:mid], num)


def test_binary_search():
    assert binary_search([1], 1) == True
    assert binary_search([1,3], 1) == True
    assert binary_search([1,3,99], 1) == True
    assert binary_search([-5,0,5,9,88], -5) == True
    assert binary_search([-5,5,9,88], -5) == True
    assert binary_search([], 2) == False
    assert binary_search([1], 2) == False
    assert binary_search([1,3], 2) == False
    assert binary_search([1,3,99], 2) == False
    assert binary_search([-5,0,5,9,88], 15) == False
    assert binary_search([-5,5,9,88], 15) == False
    assert binary_search(list(range(10000000)), 15) == True


binary_search(list(range(1000)), 15)
