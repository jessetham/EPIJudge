from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder, inorder):
    from bst_node import BstNode

    def append_node(i_lower, i_upper, p):
        if i_upper - i_lower <= 0:
            return None, p - 1
        preorder_value = preorder[p]
        inorder_index = value_index[preorder_value]
        node = BstNode(preorder_value)
        node.left, p = append_node(i_lower, inorder_index, p + 1)
        node.right, p = append_node(inorder_index + 1, i_upper, p + 1)
        return node, p

    value_index = {}
    for i, value in enumerate(inorder):
        value_index[value] = i
    node, _ = append_node(0, len(inorder), 0)
    return node



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
