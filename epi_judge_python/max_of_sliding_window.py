import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
from implementations import MinMaxQueue

class TrafficElement:
    def __init__(self, time, volume):
        self.time = time
        self.volume = volume

def calculate_traffic_volumes(A, w):
    from collections import deque
    results = []
    min_max_q = MinMaxQueue()
    time_q = deque()
    for elem in A:
        while len(min_max_q) > 0 and (elem.time - time_q[0]) > w:
            min_max_q.remove()
            time_q.popleft()
        min_max_q.push(elem.volume)
        time_q.append(elem.time)
        results.append(TrafficElement(elem.time, min_max_q.get_max()))
    return results


@enable_executor_hook
def calculate_traffic_volumes_wrapper(executor, A, w):
    A = [TrafficElement(t, v) for (t, v) in A]

    result = executor.run(functools.partial(calculate_traffic_volumes, A, w))

    return [(x.time, x.volume) for x in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_of_sliding_window.py",
                                       'max_of_sliding_window.tsv',
                                       calculate_traffic_volumes_wrapper))
