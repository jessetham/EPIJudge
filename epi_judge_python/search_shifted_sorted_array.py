from test_framework import generic_test


def search_smallest(A):
    if not A:
        return -1
    low, high = 0, len(A) - 1
    while low < high:
        mid = ((high - low) // 2) + low
        if A[mid] < A[high]:
            high = mid
        else:
            low = mid + 1
    return low


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_shifted_sorted_array.py",
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
