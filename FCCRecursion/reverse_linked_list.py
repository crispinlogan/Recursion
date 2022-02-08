"""
From https://www.youtube.com/watch?v=IJDJ0kBx2LM at ~1h09mins in
"""


def reverse_linked_list(head):#, prev=None):
    """
    Also here - this is what I used for testing
    https://leetcode.com/problems/reverse-linked-list/
    """
    # # recursive implementation - from https://leetcode.com/problems/reverse-linked-list/discuss/58429/Python-iterative-and-recursive-solution-both-O(n)-time-complexity.
    # def helper(head, node):
    #     if not head:
    #         return node
    #     tmp = head.next
    #     head.next = node
    #     return helper(tmp, head)
    # return helper(head, None)
    #
#     # alternative recursive implementation - explained well in vid
    if head is None or head.next is None:
        return head
    p = reverse_linked_list(head.next)
    head.next.next = head # you are setting the old next value point backwards (reversing linked list)
    head.next = None # stops cyclic dependencies given above line
    return p
#     # alternative recursive implementation - from https://leetcode.com/problems/reverse-linked-list/discuss/58338/Python-solution-Simple-Iterative
    # REQUIRES prev=None in reverse_linked_list args
    # if not head:
    #     return prev
    # next = head.next
    # head.next = prev
    # return reverse_linked_list(next, head)
    # # iterative implementation - from https://leetcode.com/problems/reverse-linked-list/discuss/58338/Python-solution-Simple-Iterative
    # # idea is to change next with prev, prev with current, and current with next
    # prev = None
    # curr = head
    # while curr:
    #     next = curr.next
    #     curr.next = prev
    #     prev = curr
    #     curr=next
    # return prev



# # definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

####
head_1 = ListNode(0)
head_1.next = ListNode(1)
head_1.next.next = ListNode(2)
head_1.next.next.next = ListNode(3)

# head_1_reversed = ListNode(3)
# head_1_reversed.next = ListNode(2)
# head_1_reversed.next.next = ListNode(1)
# head_1_reversed.next.next.next = ListNode(0)

####
head_2 = ListNode(3)

# head_2_reversed = ListNode(3)

####
head_3 = None

# head_3_reversed = None

def print_linked_list(head):
    while head:
        print(head.val)
        head = head.next

print_linked_list(head_1)
print_linked_list(head_2)
print_linked_list(head_3)

# def test_reverse_linked_list():
    # assert reverse_linked_list(head_1) == head_1_reversed
    # assert reverse_linked_list(head_2) == head_2_reversed
    # assert reverse_linked_list(head_3) == head_3_reversed
    # assert reverse_linked_list() ==

head_1_reversed = reverse_linked_list(head_1)
head_2_reversed = reverse_linked_list(head_2)
head_3_reversed = reverse_linked_list(head_3)

print_linked_list(head_1_reversed)
print_linked_list(head_2_reversed)
print_linked_list(head_3_reversed)
