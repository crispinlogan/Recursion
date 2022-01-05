def fn(arr, subsequences=None):
    """
    return a list of sub-list where each sub-list
    contains a subsequence of the original arr 
    TIME: O(2**N) - think of recursion tree
    SPACE: O(N) - depth of recursion tree - stack only ever has a max of N calls on it
    """
    if subsequences is None:
        subsequences = [[]]
    # base case
    if len(arr) == 0:
        return subsequences
    # recursive case
    for subsequence in subsequences.copy():
        subsequences.append(subsequence + [arr[0]])
    # print(subsequences)
    return fn(arr[1:], subsequences)


fn([3])
fn([3,1,2])


def fn(arr, subsequences=None):
    """
    return a list of sub-list where each sub-list
    contains a subsequence of the original arr 
    TIME: O(2**N) - think of recursion tree
    SPACE: O(N) - depth of recursion tree - stack only ever has a max of N calls on it
    JUST CHANGES ABOVE NOW TO PRINT INSTEAD OF RETURN LIST OF SUB-LISTS
    """
    if subsequences is None:
        subsequences = [[]]
    # base case
    if len(arr) == 0:
        print(subsequences)
        return
    # recursive case
    for subsequence in subsequences.copy():
        subsequences.append(subsequence + [arr[0]])
    # print(subsequences)
    fn(arr[1:], subsequences)


fn([3])
fn([3,1,2])



##################################################
# TRYING TO DO IT MORE LIKE THE WAY IN THE VIDEO
##################################################
def fn(arr, ind=0, subsequence=None):
    """
    This is what he does in video
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


def fn(arr, ind=0, subsequence=None, subsequences=None):
    """
    This is what he does in video
    NOW RETURN SUBSEQUENCES AS A LIST - I DECIDED TO DO THIS
    """
    if subsequence is None:
        subsequence = []
    if subsequences is None:
        subsequences = []
    # print(f's={subsequence}, {id(subsequence)}, {subsequences}')
    if ind >= len(arr):
        subsequences.append(subsequence.copy())
        print(subsequence)
        return subsequences
    subsequence.append(arr[ind])
    fn(arr, ind+1, subsequence, subsequences)
    subsequence.remove(arr[ind])
    fn(arr, ind+1, subsequence, subsequences)
    return subsequences

fn([3])
fn([3,1,2])

####
####
####
####
####
####

def fn(arr, k, ind=0, subsequence=None, subsequences=None):
    """
    This is what he does in video
    NOW RETURN SUBSEQUENCES AS A LIST - I DECIDED TO DO THIS
    NOW ONLY RETURN THE LIST OF SUBSEQUENCES WHERE SUM OF SUBSEQUENCE == A NUMBER K
    """
    if subsequence is None:
        subsequence = []
    if subsequences is None:
        subsequences = []
    # print(f's={subsequence}, {id(subsequence)}, {subsequences}')
    if ind >= len(arr):
        if sum(subsequence) == k:
            subsequences.append(subsequence.copy())
            print(subsequence)
        return subsequences
    subsequence.append(arr[ind])
    fn(arr, k, ind+1, subsequence, subsequences)
    subsequence.remove(arr[ind])
    fn(arr, k, ind+1, subsequence, subsequences)
    return subsequences

fn([3], 3)
fn([3,1,2], 3)
fn(list(range(24)), 3)

def fn(arr, k, running_sum=0, ind=0, subsequence=None, subsequences=None):
    """
    This is what he does in video
    NOW RETURN SUBSEQUENCES AS A LIST - I DECIDED TO DO THIS
    NOW ONLY RETURN THE LIST OF SUBSEQUENCES WHERE SUM OF SUBSEQUENCE == A NUMBER K
    AND OPTIMISED SO THE RUNNING SUM IS ALSO PASSED
    """
    if subsequence is None:
        subsequence = []
    if subsequences is None:
        subsequences = []
    # print(f's={subsequence}, {id(subsequence)}, {subsequences}')
    if ind >= len(arr):
        if running_sum == k:
            subsequences.append(subsequence.copy())
            print(subsequence)
        return subsequences
    subsequence.append(arr[ind])
    fn(arr, k, running_sum+arr[ind], ind+1, subsequence, subsequences)
    subsequence.remove(arr[ind])
    fn(arr, k, running_sum, ind+1, subsequence, subsequences)
    return subsequences

fn([3], 3)
fn([3,1,2], 3)
fn(list(range(20)), 3)

# DOING!!!
def fn(arr, k, running_sum=0, ind=0, subsequence=None, subsequences=None):
    """
    This is what he does in video
    (NOW RETURN SUBSEQUENCES AS A LIST - I DECIDED TO DO THIS
    NOW ONLY RETURN THE LIST OF SUBSEQUENCES WHERE SUM OF SUBSEQUENCE == A NUMBER K
    AND OPTIMISED SO THE RUNNING SUM IS ALSO PASSED)
    NOW ONLY RETURN THE FIRST SUBSEQUENCE WHERE SUM OF SUBSEQUENCE == A NUMBER K
    """
    if subsequence is None:
        subsequence = []
    if subsequences is None:
        subsequences = []
    print(f's={subsequence}, {id(subsequence)}, {subsequences}, {running_sum}')
    if ind >= len(arr):
        if running_sum == k:
            subsequences.append(subsequence.copy())
            print(subsequence)
            print('Hellooo')
            return subsequences, True
        return subsequences, False
    subsequence.append(arr[ind])
    if fn(arr, k, running_sum+arr[ind], ind+1, subsequence, subsequences)[1]:
        return subsequences, False
    subsequence.remove(arr[ind])
    if fn(arr, k, running_sum, ind+1, subsequence, subsequences)[1]:
        return subsequences, False
    return subsequences, False

fn([3], 3)
fn([3,1,2], 3)
fn(list(range(20)), 3)
