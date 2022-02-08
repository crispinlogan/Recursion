"""
From https://www.youtube.com/watch?v=IJDJ0kBx2LM at ~49mins in
I DON'T IMPLEMENT THIS AS I COULDN'T MYSELF...THAT'S OK, I JUST NEED TO KNOW
HOW IT WORKS CONCEPTUALLY...
"""

def merge_sort(arr):
    """
    We keep splitting the array until it is of length 1 (i.e. only has
    one element in it). At this point we perform a merge - this is done
    with a two-pointer approach in each of the 2 sorted arrays to be merged
    """
    return


def test_merge_sort():
    assert merge_sort([2,1,3]) == [1,2,3]
    assert merge_sort([1,4,99,-8,3]) == [-8,1,3,4,99]
    assert merge_sort([1]) == [1]
    assert merge_sort([]) == []
