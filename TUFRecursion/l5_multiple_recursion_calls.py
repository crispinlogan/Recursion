def fib(n):
    """
    return nth fibonacci number
    (the 1st and second fibonacci number is 0, 1 so series is
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55)
    """
    # base case
    if n == 0:
        return 0
    if n == 1:
        return 1
    # recursive case
    return fib(n-1) + fib(n-2)

fib(0)
fib(1)
fib(2)
fib(3)
fib(4)
fib(5)
fib(6)
fib(7)
fib(8)
fib(9)
fib(10)
fib(35)

# def fib(n, memo={}):
#     """
#     return nth fibonacci number
#     (the 1st and second fibonacci number is 0, 1 so series is
#     0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55)
#     MEMOIZED - i just did this - not yet part of course!
#     """
#     if memo is None:
#         memo = {}
#     # base case
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     # recursive case
#     if not n - 1 in memo:
#         memo[n-1] = fib(n-1) 
#     if not n - 2 in memo:
#         memo[n-2] = fib(n-2) 
#     return memo[n-1] + memo[n-1]

# fib(10)
# fib(35)

# def fib(n, memo={}):
#     """
#     return nth fibonacci number
#     (the 1st and second fibonacci number is 0, 1 so series is
#     0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55)
#     ITERATIVE - i just did this - not yet part of course!
#     """
#     if memo is None:
#         memo = {}
#     memo[0] = 0
#     memo[1] = 1
#     for i in range(2, n+1):
#         memo[i] = memo[i-1] + memo[i-1]
#     return memo[n]

# fib(10)
# fib(35)
