"""
From https://www.youtube.com/watch?v=IJDJ0kBx2LM at ~1h20mins in
"""


def merged_linked_lists(head1, head2):
    """
    Note that linked lists are sorted
    """
    if head1 is None and head2 is None:
        return None
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.val <= head2.val:
        ret = head1
        curr = head1
        head1 = head1.next
    else:
        ret = head2
        curr = head2
        head2 = head2.next

    while head1 and head2:
        if head1.val <= head2.val:
            curr.next = head1
            head1 = head1.next
            curr = curr.next
        else:
            curr.next = head2
            curr = curr.next
            head2 = head2.next

    if head1:
        curr.next = head1

    if head2:
        curr.next = head2

    return ret


def merged_linked_lists(head1, head2):
    """
    Note that linked lists are sorted
    """
    if head1 is None and head2 is None:
        return None
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.val <= head2.val:
        head1.next = merged_linked_lists(head1.next, head2)
        return head1
    else:
        head2.next = merged_linked_lists(head1, head2.next)
        return head2

