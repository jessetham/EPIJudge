from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x):
    converted_number = []
    if x == 0:
        return '0'
    elif x < 0:
        is_negative_number = True
        x *= -1
    else:
        is_negative_number = False

    while x != 0:
        converted_number.append(str(x % 10))
        x = x // 10
    if is_negative_number:
        converted_number.append('-')
    return ''.join(reversed(converted_number))


def string_to_int(s):
    if s[0] == '-':
        is_negative_number = True
    else:
        is_negative_number = False
    converted_number = 0
    for c in s[int(is_negative_number):]:
        converted_number *= 10
        converted_number += int(c)
    return converted_number * -1 if is_negative_number else converted_number


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
