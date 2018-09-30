import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0, node1):
    def get_depth(node):
        depth = 0
        while node:
            depth += 1
            node = node.parent
        return depth - 1
    node0_depth, node1_depth = get_depth(node0), get_depth(node1)
    deeper, shallower = (node0, node1) if node0_depth >= node1_depth else (node1, node0)
    # Bring the deeper node up to the shallower node's depth
    for _ in range(abs(node0_depth - node1_depth)):
        deeper = deeper.parent
    # Increment both nodes until they equal each other or if one of them becomes None
    while deeper and shallower:
        if deeper == shallower:
            break
        deeper, shallower = deeper.parent, shallower.parent
    return deeper


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor_with_parent.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
