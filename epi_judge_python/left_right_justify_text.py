from test_framework import generic_test


def justify_text(words, L):
    lines, spaces_left = distribute_words(words, L)
    justified_lines = distribute_spaces(lines, spaces_left, L)
    return [''.join(line) for line in justified_lines]

def distribute_words(words, L):
    lines, spaces_left, line = [], [], []
    spaces_available = L
    for word in words:
        if len(word) > spaces_available:
            lines.append(line.copy())
            spaces_left.append(spaces_available + 1)
            line = []
            spaces_available = L
        line.append(word)
        spaces_available -= len(word) + 1
    lines.append(line.copy())
    spaces_left.append(spaces_available + 1)
    return lines, spaces_left

def distribute_spaces(lines, spaces_left, L):
    justified_lines = []
    for i, line in enumerate(lines[:-1]):
        justified_line = []
        if len(line) == 1:
            justified_line.append(line[0])
            justified_line.extend([' '] * spaces_left[i])
            justified_lines.append(justified_line.copy())
            continue
        single_spaces = spaces_left[i] % (len(line) - 1)
        common_spaces = spaces_left[i] // (len(line) - 1)
        for word in line[:-1]:
            justified_line.append(word + ' ')
            justified_line.extend([' '] * common_spaces)
            if single_spaces > 0:
                justified_line.append(' ')
                single_spaces -= 1
        justified_line.append(line[-1])
        justified_lines.append(justified_line.copy())
    justified_line = []
    for word in lines[-1][:-1]:
        justified_line.append(word + ' ')
    justified_line.append(lines[-1][-1])
    justified_line.extend([' '] * spaces_left[-1])
    justified_lines.append(justified_line.copy())
    return justified_lines

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("left_right_justify_text.py",
                                       'left_right_justify_text.tsv',
                                       justify_text))
