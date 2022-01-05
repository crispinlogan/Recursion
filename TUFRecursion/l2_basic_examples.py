def fn(n):
    """
    print name n times
    """
    if n == 0:
        return
    print('name')
    fn(n-1)

fn(5)

def fn(n, start=1):
    """
    print from 1 to n
    """
    if start > n:
        return
    print(start)
    fn(n, start+1)

fn(8)

def fn(n, end = 1):
    """
    print from n to 1
    """
    if n < end:
        return
    print(n)
    fn(n-1, end)

fn(7)

def fn(n, start=1):
    """
    print from 1 (start) to n using backtracking - basically have
    the print after the function call so the first print is at bottom of recursion tree
    """
    # if start > n:
    #     return
    # fn(n-1, start)
    # print(n)
    if start > n:
        return
    fn(n-1, start)
    print(n)

fn(3)

def fn(n, end=1):
    """
    print from n to 1 (end) using backtracking - basically have
    the print after the function call so the first print is at bottom of recursion tree
    """
    if end > n:
        return
    fn(n, end+1)
    print(end)

fn(3)
