import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def bst_to_doubly_linked_list(tree):
    if not tree:
        return None
    tree.left = goto_left(tree.left, tree)
    tree.right = goto_right(tree.right, tree)
    while tree.left:
        tree = tree.left
    return tree

def goto_left(node, parent):
    if not node:
        return None
    if not node.left and not node.right:
        node.right = parent
        return node
    node.left = goto_left(node.left, node)
    node.right = goto_right(node.right, node)
    while node.right:
        node = node.right
    node.right = parent
    return node

def goto_right(node, parent):
    if not node:
        return None
    if not node.left and not node.right:
        node.left = parent
        return node
    node.left = goto_left(node.left, node)
    node.right = goto_right(node.right, node)
    while node.left:
        node = node.left
    node.left = parent
    return node

@enable_executor_hook
def bst_to_doubly_linked_list_wrapper(executor, tree):
    l = executor.run(functools.partial(bst_to_doubly_linked_list, tree))

    if l is not None and l.left is not None:
        raise TestFailure(
            'Function must return the head of the list. Left link must be None'
        )

    v = []
    while l:
        v.append(l.data)
        if l.right and l.right.left is not l:
            raise TestFailure('List is ill-formed')
        l = l.right

    return v


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("bst_to_sorted_list.py",
                                       'bst_to_sorted_list.tsv',
                                       bst_to_doubly_linked_list_wrapper))
