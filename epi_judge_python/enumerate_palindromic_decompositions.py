from test_framework import generic_test


def palindrome_decompositions(input):
    results = []
    generate(0, [], input, results)
    return results

def generate(i, decompositions, input, results):
    if i >= len(input):
        results.append(decompositions.copy())
        return
    r = i
    while r < len(input):
        if input[i] == input[r] and is_palindrome(i, r, input):
            decompositions.append(input[i:r+1])
            generate(r + 1, decompositions, input, results)
            decompositions.pop()
        r += 1

def is_palindrome(l, r, input):
    while l < r:
        if input[l] != input[r]:
            return False
        l += 1
        r -= 1
    return True

def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "enumerate_palindromic_decompositions.py",
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))
