from test_framework import generic_test


def number_of_ways(n, m):
    def find_ways(i, j):
        if i == 0 and j == 0:
            return 1
        if grid[i][j] == 0:
            ways_from_up = find_ways(i - 1, j) if i != 0 else 0
            ways_from_left = find_ways(i, j - 1) if j != 0 else 0
            grid[i][j] = ways_from_up + ways_from_left
        return grid[i][j]
    grid = [[0] * m for _ in range(n)]
    return find_ways(n - 1, m - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_matrix.py",
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
