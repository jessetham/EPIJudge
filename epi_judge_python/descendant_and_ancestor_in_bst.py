import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook


def pair_includes_ancestor_and_descendant_of_m(possible_anc_or_desc_0,
                                               possible_anc_or_desc_1, middle):
    if possible_anc_or_desc_0 == middle or \
        possible_anc_or_desc_1 == middle:
        return False
    is_0_anc = check_if_related(possible_anc_or_desc_0, middle)
    is_0_desc = check_if_related(middle, possible_anc_or_desc_0)
    is_1_anc = check_if_related(possible_anc_or_desc_1, middle)
    is_1_desc = check_if_related(middle, possible_anc_or_desc_1)
    if any([is_0_anc and is_1_desc, is_0_desc and is_1_anc]):
        return True
    return False

def check_if_related(ancestor, descendant):
    node = ancestor
    while node:
        if node.data == descendant.data:
            return True
        elif node.data < descendant.data:
            node = node.right
        else:
            node = node.left
    return False

@enable_executor_hook
def pair_includes_ancestor_and_descendant_of_m_wrapper(
        executor, tree, possible_anc_or_desc_0, possible_anc_or_desc_1,
        middle_idx):
    candidate0 = must_find_node(tree, possible_anc_or_desc_0)
    candidate1 = must_find_node(tree, possible_anc_or_desc_1)
    middle_node = must_find_node(tree, middle_idx)

    return executor.run(
        functools.partial(pair_includes_ancestor_and_descendant_of_m,
                          candidate0, candidate1, middle_node))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "descendant_and_ancestor_in_bst.py",
            'descendant_and_ancestor_in_bst.tsv',
            pair_includes_ancestor_and_descendant_of_m_wrapper))
