import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import (binary_tree_height,
                                              generate_inorder)
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def build_min_height_bst_from_sorted_array(A):
    from bst_node import BstNode
    def build_node(A, low, high):
        # Base case
        if high - low < 1:
            return None
        if high - low == 1:
            return BstNode(A[low])
        mid = ((high - low) // 2) + low
        node = BstNode(A[mid])
        node.left = build_node(A, low, mid)
        node.right = build_node(A, mid + 1, high)
        return node
    if len(A) == 0:
        return None
    return build_node(A, 0, len(A))


@enable_executor_hook
def build_min_height_bst_from_sorted_array_wrapper(executor, A):
    result = executor.run(
        functools.partial(build_min_height_bst_from_sorted_array, A))

    if generate_inorder(result) != A:
        raise TestFailure("Result binary tree mismatches input array")
    return binary_tree_height(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "bst_from_sorted_array.py", 'bst_from_sorted_array.tsv',
            build_min_height_bst_from_sorted_array_wrapper))
