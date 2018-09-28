from test_framework import generic_test


def search_first_of_k(A, k):
    if not A:
        return -1
    low = 0
    high = len(A) - 1
    while low < high:
        mid = ((high - low) // 2) + low
        if A[mid] < k:
            low = mid + 1
        elif A[mid] == k:
            high = mid
        else:
            high = mid - 1
    return low if A[low] == k else -1



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
