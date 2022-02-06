"""
From https://www.youtube.com/watch?v=IJDJ0kBx2LM around 17mins in
"""

def reverse_string(s: str):
    """
    Takes in a string and returns the reverse of the string
    USE RECURSION!
    """
    # base case
    if len(s) == 0:
        return ''
    # recursive case aka smallest amount of work I can do in each iteration, and
    # get closer to base case
    return s[-1] + reverse_string(s[:-1])


def test_reverse_string():
    assert reverse_string('qwertyuiop') == 'poiuytrewq'
    assert reverse_string('qwert yuiop') == 'poiuy trewq'
    assert reverse_string('    n') == 'n    '
    assert reverse_string('') == ''
    assert reverse_string(' ') == ' '
    assert reverse_string('hello') == 'olleh'
