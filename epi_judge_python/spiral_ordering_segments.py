from test_framework import generic_test


def matrix_in_spiral_order(square_matrix):
    if not square_matrix:
        return []

    inner_spiral = []
    if len(square_matrix) > 2:
        new_matrix = square_matrix[1:len(square_matrix)-1]
        new_matrix = [row[1:len(square_matrix)-1] for row in new_matrix]
        inner_spiral = matrix_in_spiral_order(new_matrix)
    if len(square_matrix) == 1:
        return square_matrix[0]

    result = []
    # Values along the top row
    result.extend(value for value in square_matrix[0])
    # Values along the right column (excluding the first value)
    result.extend(row[len(square_matrix)-1] for row in square_matrix[1:])
    # Values along the bottom row (excluding the last value)
    result.extend(value for value in reversed(square_matrix[len(square_matrix)-1][:len(square_matrix)-1]))
    # Values along the left column (excluding the first and last values)
    result.extend(row[0] for row in reversed(square_matrix[1:len(square_matrix)-1]))
    result.extend(inner_spiral)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
