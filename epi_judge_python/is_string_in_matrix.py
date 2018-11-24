from test_framework import generic_test


def is_pattern_contained_in_grid(grid, S):
    def dfs(i, j, start):
        if not inbounds(i, j) or \
            (i, j, start) in visited or \
            grid[i][j] != S[start]:
            return False
        if start == len(S) - 1:
            return True
        success = dfs(i - 1, j, start + 1) or \
            dfs(i + 1, j, start + 1) or \
            dfs(i, j - 1, start + 1) or \
            dfs(i, j + 1, start)
        if success:
            return True
        visited.add((i, j, start))
        return False

    def inbounds(i, j):
        if i >= 0 and i < len(grid) and \
            j >= 0 and j < len(grid[0]):
            return True
        return False

    # Check for empty S or grid
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if dfs(i, j, 0):
                return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_in_matrix.py",
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
