from test_framework import generic_test


def online_median(sequence):
    import heapq
    max_heap, min_heap = [], []
    medians = []
    for val in sequence:
        top_of_min = heapq.heappushpop(min_heap, val)
        heapq.heappush(max_heap, -top_of_min)
        if len(min_heap) != len(max_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        medians.append(min_heap[0] if len(min_heap) != len(max_heap)
            else (min_heap[0] - max_heap[0]) / 2)
    return medians


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("online_median.py", "online_median.tsv",
                                       online_median_wrapper))
