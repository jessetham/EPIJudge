import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0, l1):
    def get_length(l):
        length = 0
        while l:
            length, l = length + 1, l.next
        return length
    l0_length = get_length(l0)
    l1_length = get_length(l1)
    long, short = (l0, l1) if l0_length >= l1_length else (l1, l0)
    for _ in range(abs(l0_length - l1_length)):
        long = long.next
    while long and long != short:
        long, short = long.next, short.next
    return long


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(
        functools.partial(overlapping_no_cycle_lists, l0, l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_terminated_lists_overlap.py",
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
