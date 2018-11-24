from test_framework import generic_test, test_utils


def generate_power_set(S):
    removed = set()
    in_results = set()
    results = []
    generate(S, removed, in_results, results)
    return results

def generate(S, removed, in_results, results):
    current_set = tuple(s for s in S if s not in removed)
    if current_set in in_results:
        return
    in_results.add(current_set)
    results.append(list(current_set))
    for s in current_set:
        removed.add(s)
        generate(S, removed, in_results, results)
        removed.remove(s)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_set.py", 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
