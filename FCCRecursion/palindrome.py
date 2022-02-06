"""
From https://www.youtube.com/watch?v=IJDJ0kBx2LM at ~23mins in
"""

# def is_palindrome(s: str):
#     """
#     Takes a string and returns True if it is a Palindrome, False otherwise
#     """
#     # base case
#     if len(s) <= 1:
#         return True
#     # recursive case
#     return s[0] == s[-1] and is_palindrome(s[1:-1])


def is_palindrome(s: str):
    """
    Takes a string and returns True if it is a Palindrome, False otherwise
    EARLIER RETURN IF FALSE THAN ABOVE FUNCTION
    """
    # base case
    if len(s) <= 1:
        return True
    # recursive case
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    return False


def test_is_palindrome():
    assert is_palindrome('kayak') == True
    assert is_palindrome('ka y ak') == True
    assert is_palindrome('') == True
    assert is_palindrome(' ') == True
    assert is_palindrome('  ') == True
    assert is_palindrome('a') == True
    assert is_palindrome('aa') == True
    assert is_palindrome('aab') == False
    assert is_palindrome('kayak ') == False
    assert is_palindrome('kayak  ') == False
