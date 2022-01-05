def sum_one_to_n(n, sum=0):
    """
    parametrised PATTERN - the parameter is 'doing the work' and being
    passed through each recursive function call being updated each time
    """
    if n < 1:
        return sum
    print(n)
    print(sum)
    print(sum+n)
    return sum_one_to_n(n-1, sum+n)

sum_one_to_n(5)

def sum_one_to_n(n):
    """
    functional PATTERN - you just need to re-call the function with
    a smaller problem each time until reaching base case and the function
    takes care of things
    """
    if n == 1:
        return 1
    return n + sum_one_to_n(n-1)

sum_one_to_n(5)