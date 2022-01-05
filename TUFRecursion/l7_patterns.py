# # CHEEKILY USE FUNCTION FROM L6 THAT RETURNS ALL POSSIBLE SUBSEQUENCES AND THEN FILTER IT!
# # BUT THIS IS NOT OPTIMAL
# def outer_fn(arr, k):
#     def fn(arr, subsequences=None):
#         """
#         return a list of sub-list where each sub-list
#         contains a subsequence of the original arr 
#         TIME: O(2**N) - think of recursion tree
#         SPACE: O(N) - depth of recursion tree - stack only ever has a max of N calls on it
#         """
#         if subsequences is None:
#             subsequences = [[]]
#         # base case
#         if len(arr) == 0:
#             return subsequences
#         # recursive case
#         for subsequence in subsequences.copy():
#             subsequences.append(subsequence + [arr[0]])
#         # print(subsequences)
#         return fn(arr[1:], subsequences)
#     subsequences_all = fn(arr)
#     print(subsequences_all)
#     subsequences_equal_to_k = []
#     print(subsequences_equal_to_k)
#     for subsequence in subsequences_all:
#         if sum(subsequence) == k:
#             subsequences_equal_to_k.append(subsequence)
#     return subsequences_equal_to_k


# outer_fn([3], 3)
# outer_fn([3,1,2], 3)

# def fn(arr, k, subsequences=None):
#     """
#     return all sub-sequences whose sum is k
#     TIME: O(2**N) - think of recursion tree
#     SPACE: O(N) - depth of recursion tree - stack only ever has a max of N calls on it
#     JUST PRINTS EACH SUBSEQUENCE WHEN IT FINDS IT
#     """
#     if subsequences is None:
#         subsequences = [[]]
#     # base case
#     if len(arr) == 0:
#         return subsequences
#     # recursive case
#     for subsequence in subsequences.copy():
#         subsequence_to_add = subsequence + [arr[0]]
#         subsequences.append(subsequence_to_add)
#         if sum(subsequence_to_add) == k:
#             print(subsequence_to_add)
#     # return fn(arr[1:], k, subsequences)
#     fn(arr[1:], k, subsequences)

# fn([3], 3)
# fn([3,1,2], 3)
# fn(list(range(1,22)), 3)

# def fn(arr, k, subsequences=None):
#     """
#     return all sub-sequences whose sum is k
#     TIME: O(2**N) - think of recursion tree
#     SPACE: O(N) - depth of recursion tree - stack only ever has a max of N calls on it
#     JUST PRINTS EACH SUBSEQUENCE WHEN IT FINDS IT
#     """
#     if subsequences is None:
#         subsequences = [[]]
#     # base case
#     if len(arr) == 0:
#         return subsequences
#     # recursive case
#     for subsequence in subsequences.copy():
#         subsequence_to_add = subsequence + [arr[0]]
#         if sum(subsequence_to_add) < k:   # this helps to not make our subsequences massive, but doesn't change average complexity...
#             subsequences.append(subsequence_to_add)
#         if sum(subsequence_to_add) == k:
#             print(subsequence_to_add)
#     # return fn(arr[1:], k, subsequences)
#     fn(arr[1:], k, subsequences)


# fn([3], 3)
# fn([3,1,2], 3)
# fn(list(range(1,22)), 3)
# fn(list(range(1,22)), 150)

# TRY AND DO A PICK/NOT PICK MULTIPLE RECURSION TYPE SOLUTION?
# THEN TRY TO OPTIMIZE BY :
# - PASSING A SUM THAT MEANS WE DO NOT HAVE TO SUM EACH TIME - SAVES AN ORDER OF N
# - RETURNING EARLY IF SUM OF SUBSEQUENCE > K - RATHER NOT RETURNING EARLY, JUST DONT ADD TO SUBSEQUENCES



# # TRUE BIT
# def fn(arr, k, subsequences=None, found=False):
#     """
#     return all sub-sequences whose sum is k
#     TIME: O(2**N) - think of recursion tree
#     SPACE: O(N) - depth of recursion tree - stack only ever has a max of N calls on it
#     JUST PRINTS EACH SUBSEQUENCE WHEN IT FINDS IT
#     """
#     if subsequences is None:
#         subsequences = [[]]
#     # base case
#     if found == True:
#         return
#     if len(arr) == 0:
#         return subsequences, False
#     # recursive case
#     for subsequence in subsequences.copy():
#         subsequence_to_add = subsequence + [arr[0]]
#         if sum(subsequence_to_add) < k:   # this helps to not make our subsequences massive, but doesn't change average complexity...
#             subsequences.append(subsequence_to_add)
#         if sum(subsequence_to_add) == k:
#             print(subsequence_to_add)
#             return subsequences, True
#     # return fn(arr[1:], k, subsequences)
#     fn(arr[1:], k, subsequences, found)


# fn(list(range(1,22)), 3)
# fn(list(range(1,22)), 150)

# # TRUE BIT ON L6 FN
# def fn(arr, k, subsequences=None, found=False):
#     """
#     return a list of sub-list where each sub-list
#     contains a subsequence of the original arr 
#     TIME: O(2**N) - think of recursion tree
#     SPACE: O(N) - depth of recursion tree - stack only ever has a max of N calls on it
#     JUST CHANGES ABOVE NOW TO PRINT INSTEAD OF RETURN LIST OF SUB-LISTS
#     """
#     if subsequences is None:
#         subsequences = [[]]
#     # base case
#     if found == True: # return early condition
#         return
#     if len(arr) == 0:
#         print(subsequences)
#         return
#     # recursive case
#     for subsequence in subsequences.copy():
#         if subsequence + [arr[0]] == k:
#             found = True
#         subsequences.append(subsequence + [arr[0]])
#     # print(subsequences)
#     a = fn(arr[1:], k, subsequences, found)
#     if a:
#         return


# fn([3], 3)
# fn([3,1,2], 3)
# fn(list(range(1,4)), 3)
# fn(list(range(1,20)), 3)


def fn(arr, ind=0, subsequence=None):
    """
    This is what he does in video - this is from L6 - we build on this in the below examples
    """
    if subsequence is None:
        subsequence = []
    # print(f's={subsequence}, {id(subsequence)}')
    if ind >= len(arr):
        print(subsequence)
        return
    subsequence.append(arr[ind])
    fn(arr, ind+1, subsequence) # option 1: take element
    subsequence.remove(arr[ind]) # or subsequence.pop()
    fn(arr, ind+1, subsequence) # option 2: don't take element

fn([3])
fn([3,1,2])


def fn(arr, k, ind=0, subsequence=None):
    """
    print all sub-sequences whose sum is k
    TIME: O(2**N) - think of recursion tree and extra N factor due to sum each time
    SPACE: O(N) - depth of recursion tree - stack only ever has a max of N calls on it
    JUST PRINTS EACH SUBSEQUENCE WHEN IT FINDS IT
    """
    if subsequence is None:
        subsequence = []
    # print(f's={subsequence}, {id(subsequence)}')
    if ind >= len(arr):
        if sum(subsequence) == k:
            print(subsequence)
        return
    subsequence.append(arr[ind])
    fn(arr, k, ind+1, subsequence) # option 1: take element
    subsequence.remove(arr[ind]) # or subsequence.pop()
    fn(arr, k, ind+1, subsequence) # option 2: don't take element

fn([3,1,2], 3)
fn([3,1,2], 6)
fn([3,1,2,4,7], 7)
fn(list(range(1,22)), 5)
fn(list(range(1,20)), 150)

def fn(arr, k, running_sum=0, ind=0, subsequence=None):
    """
    print all sub-sequences whose sum is k
    TIME: O(2**N) - think of recursion tree
    SPACE: O(N) - depth of recursion tree - stack only ever has a max of N calls on it
    JUST PRINTS EACH SUBSEQUENCE WHEN IT FINDS IT
    NOW WITH RUNNING SUM OPTIMISATION
    """
    if subsequence is None:
        subsequence = []
    # print(f's={subsequence}, {id(subsequence)}')
    if ind >= len(arr):
        if running_sum == k:
            print(subsequence)
        return
    subsequence.append(arr[ind])
    fn(arr, k, running_sum+arr[ind], ind+1, subsequence) # option 1: take element
    subsequence.remove(arr[ind]) # or subsequence.pop()
    fn(arr, k, running_sum, ind+1, subsequence) # option 2: don't take element


fn([3,1,2], 3)
fn([3,1,2], 6)
fn([3,1,2,4,7], 7)
fn(list(range(1,20)), 5)
fn(list(range(1,20)), 150)


found = False
def fn(arr, k, running_sum=0, ind=0, subsequence=None):
    """
    print all sub-sequences whose sum is k
    TIME: O(2**N) - think of recursion tree
    SPACE: O(N) - depth of recursion tree - stack only ever has a max of N calls on it
    JUST PRINTS EACH SUBSEQUENCE WHEN IT FINDS IT
    NOW JUST PRINTS FIRST SUBSEQUENCE IT FINDS! USES A HACKY WAY (BEST NOT TO USE GLOBAL VAR IN PYTHON)
    """
    global found
    if subsequence is None:
        subsequence = []
    # print(f's={subsequence}, {id(subsequence)}')
    if ind >= len(arr):
        if running_sum == k and not found:
            found = True
            print(subsequence)
        return
    subsequence.append(arr[ind])
    fn(arr, k, running_sum+arr[ind], ind+1, subsequence) # option 1: take element
    subsequence.remove(arr[ind]) # or subsequence.pop()
    fn(arr, k, running_sum, ind+1, subsequence) # option 2: don't take element


fn([3,1,2], 3)
fn([3,1,2], 6)
fn([3,1,2,4,7], 7)
fn(list(range(1,20)), 5)
fn(list(range(1,20)), 150)


def fn(arr, k, running_sum=0, ind=0, subsequence=None):
    """
    print one sub-sequence (if one exists) whose sum is k
    TIME: O(2**N) - think of recursion tree
    SPACE: O(N) - depth of recursion tree - stack only ever has a max of N calls on it
    NOW JUST PRINTS FIRST SUBSEQUENCE IT FINDS! 
    USES A NON-HACKY WAY - GOOD PRACTICE!
    """
    if subsequence is None:
        subsequence = []
    # print(f's={subsequence}, {id(subsequence)}')
    if ind >= len(arr):
        if running_sum == k:
            print(subsequence)
            return True
        return False
    subsequence.append(arr[ind])
    if fn(arr, k, running_sum+arr[ind], ind+1, subsequence): # option 1: take element
        return True
    subsequence.remove(arr[ind]) # or subsequence.pop()
    if fn(arr, k, running_sum, ind+1, subsequence): # option 2: don't take element
        return True
    return False


fn([3,1,2], 3)
fn([3,1,2], 6)
fn([3,1,2,4,7], 7)
fn(list(range(1,20)), 5)
fn(list(range(1,20)), 150)


def fn(arr, k, running_sum=0, ind=0, subsequence=None, l=0, r=0):
    """
    count all sub-sequences whose sum is k
    TIME: O(2**N) - think of recursion tree
    SPACE: O(N) - depth of recursion tree - stack only ever has a max of N calls on it
    VERY SIMILAR TO ABOVE, BUT ADAPTED TO BE COUNT, NOT RETURN FIRST ONE THAT EQUALS K
    """
    if subsequence is None:
        subsequence = []
    # print(f's={subsequence}, {id(subsequence)}')
    if ind >= len(arr):
        if running_sum == k:
            print(subsequence)
            return 1
        return 0
    subsequence.append(arr[ind])
    l = fn(arr, k, running_sum+arr[ind], ind+1, subsequence, l, r) # option 1: take element
    subsequence.remove(arr[ind]) # or subsequence.pop()
    r = fn(arr, k, running_sum, ind+1, subsequence, l, r) # option 2: don't take element
    return l + r


fn([3,1,2], 3)
fn([3,1,2], 6)
fn([3,1,2,4,7], 7)
fn(list(range(1,20)), 5)
fn(list(range(1,20)), 150)


def fn(arr, k, running_sum=0, ind=0, l=0, r=0):
    """
    count all sub-sequences whose sum is k
    TIME: O(2**N) - think of recursion tree
    SPACE: O(N) - depth of recursion tree - stack only ever has a max of N calls on it
    VERY SIMILAR TO ABOVE, BUT ADAPTED TO BE COUNT, NOT RETURN FIRST ONE THAT EQUALS K
    NOTE: I HAVE NOW ALSO REMOVED THE SUBSEQUENCE HERE TOO
    NOTE: I COULD ALSO ADD ANOTHER BASE CASE TO RETURN EARLY IF WE GO ABOVE THE
    K - THIS ONLY WORKS IF ALL NUMBERS IN ARR ARE POSITIVE, AND WE'D JUST ADD:
    if running_sum > k:
        return 0
    AS A BASE CASE
    """
    # print(f's={subsequence}, {id(subsequence)}')
    if ind >= len(arr):
        if running_sum == k:
            return 1
        return 0
    l = fn(arr, k, running_sum+arr[ind], ind+1, l, r) # option 1: take element
    r = fn(arr, k, running_sum, ind+1, l, r) # option 2: don't take element
    return l + r


fn([3,1,2], 3)
fn([3,1,2], 6)
fn([3,1,2,4,7], 7)
fn(list(range(1,20)), 5)
fn(list(range(1,20)), 150)
