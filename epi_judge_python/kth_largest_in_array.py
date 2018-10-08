from test_framework import generic_test


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k, A):
    from random import randint
    def swap_around_pivot(A, low, high):
        pivot = randint(low, high)
        first_low = low
        # Move the pivot element to high for safekeeping
        A[pivot], A[high] = A[high], A[pivot]
        for i in range(low, high):
            if A[high] < A[i]:
                A[first_low], A[i] = A[i], A[first_low]
                first_low += 1
        # Return the pivot element to where it should be in the final
        # sorted array
        A[first_low], A[high] = A[high], A[first_low]
        return first_low
    low = 0
    high = len(A) - 1
    while high >= low:
        new_pivot = swap_around_pivot(A, low, high)
        if new_pivot == k - 1:
            return A[new_pivot]
        elif new_pivot > k - 1:
            high = new_pivot - 1
        else:
            low = new_pivot + 1
    raise IndexError

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("kth_largest_in_array.py",
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
