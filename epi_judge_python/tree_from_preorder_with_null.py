import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

from collections import namedtuple
from binary_tree_node import BinaryTreeNode

def reconstruct_preorder(preorder):
    if not preorder or preorder[0] == None:
        return None
    NodeInfo = namedtuple('NodeInfo', ['parent', 'right_child'])
    root = BinaryTreeNode(preorder[0])
    stack = [NodeInfo(root, True), NodeInfo(root, False)]
    i = 1
    while stack:
        node_info = stack.pop()
        if not preorder[i]:
            i += 1
            continue
        node = BinaryTreeNode(preorder[i])
        if node_info.right_child:
            node_info.parent.right = node
        else:
            node_info.parent.left = node
        stack.extend([NodeInfo(node, True), NodeInfo(node, False)])
        i += 1
    return root

@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_with_null.py",
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))
