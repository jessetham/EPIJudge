from test_framework import generic_test
from list_node import ListNode

def zipping_linked_list(L):
    length = get_length(L)
    if length == 1:
        return L
    mid = length // 2
    head2 = splice(L, mid)
    head2 = reverse(head2)
    return zip_lists(L, head2)

def get_length(node):
    length = 0
    while node:
        node = node.next
        length += 1
    return length

def splice(node, mid):
    prev = ListNode(None)
    prev.next = node
    for _ in range(mid):
        node = node.next
        prev = prev.next
    prev.next = None
    return node

def reverse(node):
    prev = None
    while node:
        next = node.next
        node.next = prev
        prev = node
        node = next
    return prev

def zip_lists(h1, h2):
    def append(n1, n2):
        n1.next = n2
        n2 = n2.next
        n1 = n1.next
        return n1, n2
    dummy = ListNode(None)
    node = dummy
    while h1 and h2:
        node, h1 = append(node, h1)
        node, h2 = append(node, h2)
    while h1:
        node, h1 = append(node, h1)
    while h2:
        node, h2 = append(node, h2)
    return dummy.next

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("zip_list.py", 'zip_list.tsv',
                                       zipping_linked_list))
