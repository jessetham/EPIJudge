from test_framework import generic_test


def even_odd_merge(L):
    from list_node import ListNode
    even, odd = ListNode(), ListNode()
    even_runner, odd_runner = even, odd
    parity = 0
    while L:
        if parity % 2 == 0:
            even_runner.next = L
            even_runner = even_runner.next
        else:
            odd_runner.next = L
            odd_runner = odd_runner.next
        parity ^= 1
        L = L.next
    even_runner.next = odd.next
    odd_runner.next = None
    return even.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("even_odd_list_merge.py",
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
