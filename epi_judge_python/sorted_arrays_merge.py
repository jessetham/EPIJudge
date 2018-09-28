from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays):
    import heapq
    from collections import namedtuple
    result = []
    min_heap = []
    ArrayValue = namedtuple('ArrayValue', ['value', 'array', 'position'])
    for i, array in enumerate(sorted_arrays):
        heapq.heappush(min_heap, ArrayValue(array[0], i, 0))

    while min_heap:
        value = heapq.heappop(min_heap)
        result.append(value.value)
        if value.position < len(sorted_arrays[value.array]) - 1:
            array = sorted_arrays[value.array]
            heapq.heappush(min_heap, ArrayValue(array[value.position+1], value.array, value.position + 1))
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
