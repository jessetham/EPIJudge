import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0, node1):
    def is_parent_lca(node):
        if node in seen_nodes:
            return node, True
        seen_nodes.add(node)
        return node.parent, False

    seen_nodes = set()
    while node0 != None and node1 != None:
        node0, found0 = is_parent_lca(node0)
        node1, found1 = is_parent_lca(node1)
        if found0 or found1:
            return node0 if found0 else node1
    while node0 != None:
        node0, found0 = is_parent_lca(node0)
        if found0:
            return node0
    while node1 != None:
        node1, found1 = is_parent_lca(node1)
        if found1:
            return node1

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
        generic_test.generic_test_main(
            "lowest_common_ancestor_close_ancestor.py",
            'lowest_common_ancestor.tsv', lca_wrapper))
