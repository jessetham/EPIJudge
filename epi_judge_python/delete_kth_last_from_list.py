from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):
    if not L:
        return None

    # Move the fast pointer up k spaces
    fast = L
    for _ in range(k):
        if not fast:
            raise Exception
        fast = fast.next
    prev_slow, slow = None, L
    while fast:
        prev_slow = slow
        slow, fast = slow.next, fast.next
    if not prev_slow:
        return slow.next
    else:
        prev_slow.next = slow.next
        return L



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
