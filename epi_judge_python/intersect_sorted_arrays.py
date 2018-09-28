from test_framework import generic_test

# For when A is a magnitude smaller or larger than B
def intersect_two_sorted_arrays_1(A, B):
    smaller_arr, larger_arr = (A, B) if len(A) < len(B) else (B, A)
    current_key = None
    result = []
    for i in range(len(smaller_arr)):
        if smaller_arr[i] != current_key:
            current_key = smaller_arr[i]
            low = 0
            high = len(larger_arr) - 1
            while low <= high:
                mid = ((high - low) // 2) + low
                if larger_arr[mid] < current_key:
                    low = mid + 1
                elif larger_arr[mid] == current_key:
                    result.append(current_key)
                    break
                else:
                    high = mid - 1
    return result

# For when A and B are about the same size
def intersect_two_sorted_arrays_2(A, B):
    def move_to_next_val(arr, current_index):
        current_val = arr[current_index]
        new_index = current_index
        while new_index < len(arr) and arr[new_index] == current_val:
            new_index += 1
        return new_index
    result = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            result.append(A[i])
            i = move_to_next_val(A, i)
            j = move_to_next_val(B, j)
        elif A[i] < B[j]:
            i = move_to_next_val(A, i)
        else:
            j = move_to_next_val(B, j)
    return result


def intersect_two_sorted_arrays(A, B):
    return intersect_two_sorted_arrays_2(A, B)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
