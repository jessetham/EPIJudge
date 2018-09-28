from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    from collections import Counter
    letter_text, magazine_text = str(letter_text), str(magazine_text)
    # Count the characters in the magazine text
    mag_char_count = Counter(magazine_text)
    for c in letter_text:
        if c not in mag_char_count or mag_char_count[c] == 0:
            return False
        else:
            mag_char_count[c] -= 1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
