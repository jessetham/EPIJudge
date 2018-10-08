from test_framework import generic_test


def square_root(k):
    low = 0
    high = k
    while low <= high:
        mid = ((high - low) // 2) + low
        mid_squared = mid ** 2
        if mid_squared < k:
            low = mid + 1
        elif mid_squared == k:
            return mid
        else:
            high = mid - 1
    return low - 1



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_square_root.py",
                                       "int_square_root.tsv", square_root))
