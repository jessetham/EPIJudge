from test_framework import generic_test


def plus_one(A):
    i = len(A) - 1
    carry_over = True
    while i >= 0 and carry_over:
        A[i] += 1
        if A[i] == 10:
            A[i] %= 10
            carry_over = True
        else:
            carry_over = False
        i -= 1
    if carry_over:
        A.insert(0, 1)
    return A



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
