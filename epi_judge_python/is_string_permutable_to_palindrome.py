from test_framework import generic_test


def can_form_palindrome(s):
    if not s:
        return True
    from collections import Counter
    char_count = Counter(s)
    number_of_odd_counts = 0
    for char, count in char_count.items():
        if count % 2 != 0:
            number_of_odd_counts += 1
    return True if number_of_odd_counts < 2 else False



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
