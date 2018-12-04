import collections

from test_framework import generic_test

Interval = collections.namedtuple('Interval', ('left', 'right'))


def range_lookup_in_bst(tree, interval):
    results = []
    search_range(interval.left, interval.right, tree, results)
    return results

def search_range(l, r, node, results):
    if not node:
        return
    if l < node.data and r < node.data:
        search_range(l, r, node.left, results)
    elif l > node.data and r > node.data:
        search_range(l, r, node.right, results)
    else:
        search_range(l, node.data, node.left, results)
        results.append(node.data)
        search_range(node.data, r, node.right, results)

def range_lookup_in_bst_wrapper(tree, i):
    return range_lookup_in_bst(tree, Interval(*i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("range_lookup_in_bst.py",
                                       'range_lookup_in_bst.tsv',
                                       range_lookup_in_bst_wrapper))
