from test_framework import generic_test


def is_palindrome(s):
    def index_of_next_alphanum(i, reverse=False):
        limit = len(s) if not reverse else -1
        while i != limit:
            if s[i].isalnum():
                return i
            i += 1 if not reverse else -1
        return limit
    if not s:
        return True
    low = index_of_next_alphanum(0)
    high = index_of_next_alphanum(len(s) - 1, reverse=True)
    while high > low:
        if s[high].lower() != s[low].lower():
            return False
        low = index_of_next_alphanum(low + 1)
        high = index_of_next_alphanum(high - 1, reverse=True)
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_palindromic_punctuation.py",
                                       "is_string_palindromic_punctuation.tsv",
                                       is_palindrome))
