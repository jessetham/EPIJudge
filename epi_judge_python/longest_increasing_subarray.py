import collections

from test_framework import generic_test

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_longest_increasing_subarray(A):
    l, max_window = 0, Subarray(0, 0)
    prev = float('-inf')
    for i, val in enumerate(A):
        if prev >= val:
            l = i
        max_window = Subarray(l, i) if (i - l + 1) > (max_window.end - max_window.start + 1) \
            else max_window
        prev = val
    return max_window


def find_longest_increasing_subarray_wrapper(A):
    result = find_longest_increasing_subarray(A)
    return result.end - result.start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_increasing_subarray.py",
            'longest_increasing_subarray.tsv',
            find_longest_increasing_subarray_wrapper))
