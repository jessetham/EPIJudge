from test_framework import generic_test

# Counting/distribution sort
def majority_search_1(stream):
    from collections import defaultdict
    counter = defaultdict(int)
    for c in stream:
        counter[c] += 1
    majority_elem, highest_count = None, 0
    for key, count in counter.items():
        if count > highest_count:
            majority_elem = key
            highest_count = count
    return majority_elem

# O(1) solution by taking advantage of a priori knowledge
def majority_search_2(stream):
    majority_elem = stream.__next__()
    count = 1
    for c in stream:
        if c == majority_elem:
            count += 1
        else:
            count -= 1
            if count == 0:
                majority_elem = c
                count = 1
    return majority_elem

def majority_search_wrapper(stream):
    return majority_search_2(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("majority_element.py",
                                       'majority_element.tsv',
                                       majority_search_wrapper))
