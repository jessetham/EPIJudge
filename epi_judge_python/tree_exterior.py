import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def exterior_binary_tree(tree):
    if not tree:
        return []

    result = [tree]
    # Get left exterior
    node = tree.left
    while node and (node.left is not node.right):
        result.append(node)
        node = node.left if node.left else node.right
    # Get leaves
    stack = [tree]
    while stack:
        node = stack.pop()
        if node.left == None and node.right == None and node is not tree:
            result.append(node)
            continue
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    # Get right exterior
    node = tree.right
    while node and (node.right is not node.left):
        stack.append(node)
        node = stack[-1].right if stack[-1].right else stack[-1].left
    result.extend(reversed(stack))
    return result

def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_exterior.py", 'tree_exterior.tsv',
                                       create_output_list_wrapper))
