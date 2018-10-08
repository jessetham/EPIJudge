from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree, k):
    def inorder_traversal(node, k_largest, k):
        if not node:
            return
        inorder_traversal(node.right, k_largest, k)
        if len(k_largest) == k:
            return
        k_largest.append(node.data)
        inorder_traversal(node.left, k_largest, k)
    k_largest = []
    inorder_traversal(tree, k_largest, k)
    return k_largest


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))
