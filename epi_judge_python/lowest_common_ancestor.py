import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(tree, node0, node1):
    def dfs(node, target, path):
        if not node:
            return False
        if node.data == target.data:
            path.append(node)
            return True
        # Recurse with dfs to look for the target
        if dfs(node.left, target, path) or dfs(node.right, target, path):
            path.append(node)
            return True
        else:
            return False

    node0_path, node1_path = [], []
    # Could use the return booleans to confirm that there is a path if we
    # wanted to
    is_path_to_node0 = dfs(tree, node0, node0_path)
    is_path_to_node1 = dfs(tree, node1, node1_path)

    last_common_node = None
    for node_in_path0, node_in_path1 in zip(reversed(node0_path), reversed(node1_path)):
        if node_in_path0 != node_in_path1:
            break
        last_common_node = node_in_path0
    return last_common_node



@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
