import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from test_framework.test_utils import enable_executor_hook

HighwaySection = collections.namedtuple('HighwaySection',
                                        ('x', 'y', 'distance'))


def find_best_proposals(H, P, n):
    best_proposal = None
    best_savings = 0
    min_distances = floyd_warshall(H, n)
    for x, y, distance in P:
        savings = 0
        for i in range(n):
            for j in range(n):
                difference = min_distances[i][j] - (min_distances[i][x] + distance + min_distances[y][j])
                savings += difference if difference > 0 else 0
        if savings > best_savings:
            best_savings = savings
            best_proposal = HighwaySection(x, y, distance)
    return best_proposal

def floyd_warshall(edges, n):
    min_distances = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        min_distances[i][i] = 0
    for x, y, distance in edges:
        min_distances[x][y] = min_distances[y][x] = distance
    for k in range(n):
        for i in range(n):
            for j in range(n):
                min_distances[i][j] = min_distances[j][i] = min(
                    min_distances[i][j],
                    min_distances[i][k] + min_distances[k][j]
                )
    return min_distances

@enable_executor_hook
def find_best_proposals_wrapper(executor, H, P, n):
    H = [HighwaySection(*x) for x in H]
    P = [HighwaySection(*x) for x in P]

    return executor.run(functools.partial(find_best_proposals, H, P, n))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "road_network.py",
            'road_network.tsv',
            find_best_proposals_wrapper,
            res_printer=res_printer))
