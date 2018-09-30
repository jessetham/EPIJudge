from test_framework import generic_test


def reverse_sublist(L, start, finish):
    if not L:
        return

    from collections import namedtuple
    ListNode = namedtuple('ListNode', ['data', 'next'])

    s = iter(L)
    before_rev = ListNode(None, s)
    for _ in range(1, start):
        s = s.next
        before_rev = before_rev.next

    dummy_prev, dummy = s, s.next
    for _ in range(start, finish):
        temp = dummy.next
        dummy.next = dummy_prev
        dummy_prev = dummy
        dummy = temp

    start.next = dummy
    before_rev.next = dummy_prev


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
