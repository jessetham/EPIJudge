from test_framework import generic_test


def merge_two_sorted_arrays(A, m, B, n):
    # Copy the remaining values from one array to another. Returns
    # the new position for the to index
    def fill_remaining_elements(fr, i, to, j):
        while i >= 0:
            to[j] = fr[i]
            j -= 1
            i -= 1
        return j
    i, j = m - 1, n - 1
    beginning = len(A) - 1
    while i >= 0 and j >= 0:
        if A[i] > B[j]:
            A[beginning] = A[i]
            i -= 1
        else:
            A[beginning] = B[j]
            j -= 1
        beginning -= 1
    beginning = fill_remaining_elements(A, i, A, beginning)
    beginning = fill_remaining_elements(B, j, A, beginning)



def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sorted_arrays_merge.py",
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
