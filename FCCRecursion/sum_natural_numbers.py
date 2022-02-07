"""
From https://www.youtube.com/watch?v=IJDJ0kBx2LM at ~35mins in
"""

def sum_natural_numbers(num: int):
    """
    Takes an int and sums up all integers from 1 to that number
    """
    if num == 0:
        return 0
    return num + sum_natural_numbers(num - 1)


def test_sum_natural_numbers():
    assert sum_natural_numbers(1) == 1
    assert sum_natural_numbers(2) == 3
    assert sum_natural_numbers(3) == 6
    assert sum_natural_numbers(4) == 10
    assert sum_natural_numbers(5) == 15
    assert sum_natural_numbers(6) == 21
    assert sum_natural_numbers(7) == 28
    assert sum_natural_numbers(8) == 36
    assert sum_natural_numbers(9) == 45
    assert sum_natural_numbers(10) == 55

sum_natural_numbers(6)
