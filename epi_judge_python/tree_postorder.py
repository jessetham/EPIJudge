from test_framework import generic_test


# We use stack and previous node pointer to simulate postorder traversal.
def postorder_traversal(tree):
    if not tree:
        return []
    stack, preorder = [], []
    stack.append(tree)
    while stack:
        node = stack.pop()
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
        preorder.append(node.data)
    return list(reversed(preorder))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "tree_postorder.py", 'tree_postorder.tsv', postorder_traversal))
