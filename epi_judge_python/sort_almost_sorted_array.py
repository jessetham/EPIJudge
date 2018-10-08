from test_framework import generic_test

# So when we say that an element is no more than k away from its proper spot we
# have to store k * 2 + 1 values right? Cause it could be k elements to the left or right
# of where it is right now. That still gives us O(nlgk), which is better than the O(nlgn) if
# we just sorted the whole array. Also our space complexity would be O(k), which is way better than
# loading all n values into memory to sort it (assuming you don't count the output list as space)
def sort_approximately_sorted_array(sequence, k):
    import heapq
    min_heap = []
    result = []
    for _ in range(k + 1):
        try:
            heapq.heappush(min_heap, sequence.__next__())
        except StopIteration:
            break
    for value in sequence:
        result.append(heapq.heappop(min_heap))
        heapq.heappush(min_heap, value)
    while min_heap:
        result.append(heapq.heappop(min_heap))
    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
