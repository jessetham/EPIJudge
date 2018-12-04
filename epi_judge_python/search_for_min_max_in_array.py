import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))

def find_min_max(A):
    return find_min_max_1(A)

def find_min_max_1(A):
    if len(A) == 0:
        return None
    low_so_far, high_so_far = A[0], A[0]
    for i in range(1, len(A)):
        if A[i] < low_so_far:
            low_so_far = A[i]
        elif A[i] > high_so_far:
            high_so_far = A[i]
    return MinMax(low_so_far, high_so_far)

def res_printer(prop, value):
    def fmt(x):
        return 'min: {}, max: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_for_min_max_in_array.py",
            'search_for_min_max_in_array.tsv',
            find_min_max,
            res_printer=res_printer))
