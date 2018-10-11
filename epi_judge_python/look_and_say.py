from test_framework import generic_test


def look_and_say(n):
    if n < 1:
        raise Exception('n needs to be greater than 0')
    old_sequence = '1'
    for _ in range(n - 1):
        next_sequence = []
        i, first_unique = 0, 0
        while i < len(old_sequence):
            while i < len(old_sequence) and \
                old_sequence[first_unique] == old_sequence[i]:
                i += 1
            next_sequence.extend([str(i - first_unique),
                str(old_sequence[first_unique])])
            first_unique = i
        old_sequence = ''.join(next_sequence)
    return old_sequence


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("look_and_say.py", "look_and_say.tsv",
                                       look_and_say))
