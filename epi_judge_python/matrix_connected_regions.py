from test_framework import generic_test


def flip_color(x, y, image):
    def dfs(x, y):
        if not inbounds(x, y) or image[x][y] != color:
            return
        image[x][y] ^= 1
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)

    def inbounds(x, y):
        if x >= 0 and x < len(image) and y >= 0 and y < len(image[0]):
            return True
        return False

    if not image:
        return
    color = image[x][y]
    dfs(x, y)


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_connected_regions.py",
                                       'painting.tsv', flip_color_wrapper))
