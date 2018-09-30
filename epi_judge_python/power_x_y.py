from test_framework import generic_test


def power(x, y):
    result = 1.
    if y < 0:
        negative_exponential = True
        y *= -1
    else:
        negative_exponential = False
    while y > 0:
        result *= x
        y -= 1
    return 1 / result if negative_exponential else result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_x_y.py", 'power_x_y.tsv', power))
