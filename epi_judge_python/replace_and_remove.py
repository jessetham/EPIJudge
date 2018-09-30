import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size, s):
    new_arr_i, old_arr_i, num_a = 0, 0, 0
    while old_arr_i < size:
        if s[old_arr_i] != 'b':
            s[new_arr_i] = s[old_arr_i]
            new_arr_i += 1
        if s[old_arr_i] == 'a':
            num_a += 1
        old_arr_i += 1

    new_size = new_arr_i + num_a
    i = new_size - 1
    for j in reversed(range(new_arr_i)):
        if s[j] == 'a':
            s[i], s[i-1] = 'd', 'd'
            i -= 2
        else:
            s[i] = s[j]
            i -= 1
    return new_size



@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
