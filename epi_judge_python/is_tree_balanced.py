from test_framework import generic_test


def is_balanced_binary_tree(tree):
    # if not tree:
        # raise Exception
    def if_balanced_binary_tree_helper(node):
        if not node:
            return -1
        left_subtree_height = if_balanced_binary_tree_helper(node.left)
        right_subtree_height = if_balanced_binary_tree_helper(node.right)
        height_difference = abs(left_subtree_height - right_subtree_height)
        if height_difference > 1:
            return float('inf')
        else:
            return max(left_subtree_height, right_subtree_height) + 1
    return if_balanced_binary_tree_helper(tree) != float('inf')



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
