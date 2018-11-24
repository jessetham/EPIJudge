from test_framework import generic_test


def is_well_formed(s):
    if not s:
        return True
    stack = []
    open_brackets = set(['{', '(', '['])
    brackets_map = {
        '}': '{',
        ')': '(',
        ']': '['
    }
    for c in s:
        if c in open_brackets:
            stack.append(c)
        elif c in brackets_map:
            if not stack or stack.pop() != brackets_map[c]:
                return False
    return False if stack else True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_parenthesization.py",
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
