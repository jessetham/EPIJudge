from test_framework import generic_test, test_utils


def permutations(A):
    if not A:
        return []
    candidates = [False] * len(A)
    results = []
    generate(A, candidates, [], results)
    return results

def generate(A, candidates, permutation, results):
    if len(permutation) == len(A):
        results.append(permutation.copy())
        return
    for i in range(len(A)):
        if candidates[i] == False:
            candidates[i] = True
            permutation.append(A[i])
            generate(A, candidates, permutation, results)
            permutation.pop()
            candidates[i] = False

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("permutations.py", 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
