import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items, capacity):
    dp = [[0] * (capacity + 1) for _ in range(len(items) + 1)]
    for i in range(1, len(items) + 1):
        weight = items[i-1].weight
        value = items[i-1].value
        for j in range(1, capacity + 1):
            if weight <= j:
                max_value = max(
                    dp[i-1][j - weight] + value,
                    dp[i-1][j]
                )
            else:
                max_value = dp[i-1][j]
            dp[i][j] = max_value
    return dp[len(items)][capacity]


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("knapsack.py", "knapsack.tsv",
                                       optimum_subject_to_capacity_wrapper))
