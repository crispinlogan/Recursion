"""
From https://www.youtube.com/watch?v=IJDJ0kBx2LM at ~44mins in
"""

# def fib(n):
#     """
#     0, 1, 1, 2, 3, 5, 8, 13, 21, 34
#     """
#     # base case
#     if n <= 1:
#         return n
#     # recursive case
#     return fib(n-1) + fib(n-2)

def fib(n, memo=None):
    """
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34
    Memoized
    """
    if memo is None:
        memo = {}
    # base case
    if n <= 1:
        return n
    # recursive case
    if n-1 in memo:
        f1 = memo[n-1]
    else:
        f1 = fib(n-1, memo)
        memo[n-1] = f1
    if n-2 in memo:
        f2 = memo[n-2]
    else:
        f2 = fib(n-2, memo)
        memo[n-2] = f2
    return f1 + f2

def fib(n, memo=None):
    """
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34
    Memoized and cleaner
    """
    if memo is None:
        memo = {}
    # base case
    if n <= 1:
        return n
    # recursive case
    if n-1 not in memo:
        memo[n-1] = fib(n-1, memo)
    if n-2 not in memo:
        memo[n-2] = fib(n-2, memo)
    return memo[n-1] + memo[n-2]

def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(5) == 5

print(fib(50))
