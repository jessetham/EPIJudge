from test_framework import generic_test
from binary_tree_node import BinaryTreeNode

def rebuild_bst_from_preorder(preorder_sequence):
    if not preorder_sequence:
        return None
    root, _ = reconstruct(preorder_sequence, 0, float('-inf'), float('inf'))
    return root

def reconstruct(preorder, i, lb, ub):
    node = BinaryTreeNode(data=preorder[i])
    if i + 1 < len(preorder) and preorder[i+1] < node.data and \
        preorder[i+1] > lb:
        node.left, i = reconstruct(preorder, i + 1, lb, node.data)
    if i + 1 < len(preorder) and preorder[i+1] > node.data and \
        preorder[i+1] < ub:
        node.right, i = reconstruct(preorder, i + 1, node.data, ub)
    return node, i

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("bst_from_preorder.py",
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
