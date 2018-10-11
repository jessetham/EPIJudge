import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a string encoded as bytearray.
def reverse_words(s):
    def reverse(s, low, high):
        while low < high:
            s[low], s[high] = s[high], s[low]
            low, high = low + 1, high - 1

    def find_word_bounds(s, start):
        while start < len(s) and s[start] == ord(' '):
            start += 1
        low = start
        while start < len(s) and s[start] != ord(' '):
            start += 1
        return low, start

    # First, reverse the entire string
    low, high = 0, len(s) - 1
    reverse(s, low, high)
    # Next, reverse each individual word in the bytearray
    start = 0
    while start < len(s):
        low, start = find_word_bounds(s, start)
        reverse(s, low, start - 1)


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = bytearray()
    s_copy.extend(map(ord, s))

    executor.run(functools.partial(reverse_words, s_copy))

    return s_copy.decode("utf-8")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_words.py", 'reverse_words.tsv',
                                       reverse_words_wrapper))
