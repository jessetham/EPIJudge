from test_framework import generic_test

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_two_sorted_lists(L1, L2):
    dummy = ListNode(None)
    head = dummy
    while L1 and L2:
        if L1.data <= L2.data:
            dummy.next = L1
            L1 = L1.next
        else:
            dummy.next = L2
            L2 = L2.next
        dummy = dummy.next
    dummy.next = L1 if not L2 else L2
    return head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
