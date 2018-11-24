from test_framework import generic_test


def fill_surrounded_regions(board):
    def outside_traversal():
        for j in range(len(board[0]) - 1):
            if board[0][j] == 'W':
                q.append((0, j))
        for i in range(len(board) - 1):
            if board[i][len(board[0])-1] == 'W':
                q.append((i, len(board[0]) - 1))
        for i in reversed(range(1, len(board[0]))):
            if board[len(board)-1][i] == 'W':
                q.append((len(board) - 1, i))
        for i in reversed(range(1, len(board))):
            if board[i][0] == 'W':
                q.append((i, 0))

    def bfs():
        while q:
            row, col = q.popleft()
            if out_of_bounds(row, col) or board[row][col] != 'W':
                continue
            q.extend([(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)])
            board[row][col] = 'T'

    def out_of_bounds(x, y):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            return True
        return False

    from collections import deque
    q = deque()
    outside_traversal()
    bfs()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'W': board[i][j] = 'B'
            elif board[i][j] == 'T': board[i][j] = 'W'


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_enclosed_regions.py",
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
