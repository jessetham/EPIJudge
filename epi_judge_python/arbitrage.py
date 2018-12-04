from test_framework import generic_test
from math import log10

def is_arbitrage_exist(graph):
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            graph[i][j] = -log10(graph[i][j])
    return bellman_ford(graph)

def bellman_ford(graph):
    n = len(graph)
    predecessor = [None] * n
    distance = [float('inf')] * n
    distance[0] = 0
    for _ in range(n):
        for i in range(len(graph)):
            for j in range(len(graph[0])):
                distance[j] = min(distance[j], distance[i] + graph[i][j])

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if distance[j] > distance[i] + graph[i][j]:
                return True
    return False

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("arbitrage.py", "arbitrage.tsv",
                                       is_arbitrage_exist))
