from test_framework import generic_test


def binary_tree_depth_order(tree):
    if not tree:
        return []

    from collections import deque
    q = deque()
    result = []
    q.appendleft((tree, 0))

    while q:
        node, depth = q.pop()
        if depth == len(result):
            result.append([])
        result[depth].append(node.data)
        if node.left:
            q.appendleft((node.left, depth + 1))
        if node.right:
            q.appendleft((node.right, depth + 1))
    return result



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
