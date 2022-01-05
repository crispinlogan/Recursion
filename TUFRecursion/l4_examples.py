def fn(arr):
    """
    reverse array
    """
    if arr == []:
        return []
    return fn(arr[1:]) + [arr[0]]


fn([1,2,4,3])
# fn([1,2,4,3]) -> [3, 4, 2, 1]
# fn([2,4,3]) -> [3, 4, 2]
# fn([4,3]) -> [3, 4]
# fn([3]) -> [3]
# fn([]) -> []

def fn(arr, a=0, b=None):
    """
    reverse array - but this time we do it in place
    """
    # initialise end pointer - only first time fn is called
    if b is None:
        b = len(arr) - 1
    # base case
    if a == b or b < a:
        return arr
    # recursive case
    arr[a], arr[b] = arr[b], arr[a]
    return fn(arr, a + 1, b - 1)

fn([1,2,4,3,5]) 

fn([1,2,4,3]) 
# fn([1,2,4,3], 0, None)
# fn([3,2,4,1], 1, 2)
# fn([3,4,2,1], 2, 1) -> return [3, 4, 2, 1] 

def fn(arr):
    """
    reverse array - but this time we do it in place AND NICER CODE WITHOUT PARAMETERS BY USING A HELPER
    """
    def helper(arr, a, b):
        # base case
        if a == b or b < a:
            return arr
        # recursive case
        arr[a], arr[b] = arr[b], arr[a]
        return helper(arr, a + 1, b - 1)
    return helper(arr, 0, len(arr) - 1)

fn([1,2,4,3,5]) 

fn([1,2,4,3]) 

def fn(arr):
    """
    reverse array - but this time we do it in place AND NICER CODE WITHOUT PARAMETERS BY USING A HELPER
    AND WITH A SINGLE 'POINTER' - not necessary really but trying different things!
    """
    def helper(arr, a=0):
        # base case
        if a >= len(arr) // 2:
            return arr
        # recursive case
        arr[a], arr[-1 - a] = arr[-1 - a], arr[a]
        return helper(arr, a + 1)
    return helper(arr, 0)

fn([1,2,4,3,5]) 

fn([1,2,4,3]) 

def fn(string):
    """
    check if string a palindrome
    """
    # base case
    if len(string) <= 1:
        return True
    # recursive case
    # return (string[0] == string[-1]) and fn(string[1:-1])
    if string[0] != string[-1]:
        return False
    return fn(string[1:-1])

fn('hello') # False
# fn('hello') -> return False straight away

fn('abhhba') # True
# fn('abhhba') -> 
# fn('bhhb') ->
# fn('hh') -> 
# fn('') -> True

fn('abhthba') # True
fn('abhtqhba') # False
fn('abhtqhbag') # False
