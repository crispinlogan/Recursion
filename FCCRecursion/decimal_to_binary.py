"""
From https://www.youtube.com/watch?v=IJDJ0kBx2LM at ~28mins in

e.g. What is 13 in decimal in binary?

13 // 2 = 6 rem 1
6 // 2 = 3 rem 0
3 // 2 = 1 rem 1
1 // 2 = 0 rem 1
0 // 2 so stop

so take rems and you see it is 1101

Using recursive calls

fn(//2) returns ''
fn(1//2) + '1'
fn(3//2) + '1'
fn(6//2) + '0'
fn(13//2) + '1'

"""

def decimal_to_binary(num: int, ans=''):
    """
    Takes an int and converts it from decimal to binary and returns it
    Solution is from vid and also explained here:
    https://www.cuemath.com/numbers/decimal-to-binary/
    """
    # # non-recursive way
    # if num == 0:
    #     return 0
    # quotient = num
    # ans = ''
    # while quotient > 0:
    #     new_quotient = quotient // 2
    #     rem = quotient % 2
    #     # print(rem)
    #     ans += str(rem)
    #     quotient = new_quotient
    # return int(ans[::-1])
    #
    #
    # # recursive way
    # # base case
    # if num == 0:
    #     return ''
    # # recursive case
    # return decimal_to_binary(num // 2) + str(num % 2)
    #
    # recursive way that does deal with 0 and negative inputs and returns an int
    def helper(num):
        # base case
        if num == 0:
            return ''
        # recursive case
        return helper(num // 2) + str(num % 2)
    if num == 0:
        return 0
    if num < 0:
        return -int(helper(-num))
    return int(helper(num))


def test_decimal_to_binary():
    assert decimal_to_binary(0) == 0
    assert decimal_to_binary(1) == 1
    assert decimal_to_binary(2) == 10
    assert decimal_to_binary(3) == 11
    assert decimal_to_binary(4) == 100
    assert decimal_to_binary(5) == 101
    assert decimal_to_binary(6) == 110
    assert decimal_to_binary(7) == 111
    assert decimal_to_binary(8) == 1000
    assert decimal_to_binary(9) == 1001
    assert decimal_to_binary(10) == 1010
    assert decimal_to_binary(11) == 1011
    assert decimal_to_binary(12) == 1100

decimal_to_binary(13)
