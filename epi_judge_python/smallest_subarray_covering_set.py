import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set(paragraph, keywords):
    from collections import defaultdict
    right, left = 0, 0
    min_subwindow_size = float('inf')
    result = None
    seen_keywords = defaultdict(int)
    seen_unique_keywords = len(keywords)

    while right < len(paragraph):
        # Adding keywords loop
        while seen_unique_keywords > 0 and right < len(paragraph):
            new_word = paragraph[right]
            if new_word in keywords:
                seen_keywords[new_word] += 1
                if seen_keywords[new_word] == 1:
                    seen_unique_keywords -= 1
            right += 1

        # Removing keywords loop
        while seen_unique_keywords == 0:
            if right - left < min_subwindow_size:
                result = Subarray(left, right - 1)
                min_subwindow_size = right - left
            new_word = paragraph[left]
            if new_word in keywords:
                seen_keywords[new_word] -= 1
                if seen_keywords[new_word] == 0:
                    seen_unique_keywords += 1
            left += 1

    return result

@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure("Index out of range")

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure("Not all keywords are in the range")

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "smallest_subarray_covering_set.py",
            "smallest_subarray_covering_set.tsv",
            find_smallest_subarray_covering_set_wrapper))
