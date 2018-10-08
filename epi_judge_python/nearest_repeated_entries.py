from test_framework import generic_test


def find_nearest_repetition(paragraph):
    class WordStats:
        def __init__(self, last_seen_index):
            self.last_seen_index = last_seen_index
            self.current_min_distance = float('inf')
    word_stats_map = {}
    for i, word in enumerate(paragraph):
        if word not in word_stats_map:
            word_stats_map[word] = WordStats(i)
        else:
            word_stats_map[word].current_min_distance = \
                min(word_stats_map[word].current_min_distance, i - word_stats_map[word].last_seen_index)
            word_stats_map[word].last_seen_index = i
    min_so_far = float('inf')
    for word, stats in word_stats_map.items():
        min_so_far = min(min_so_far, stats.current_min_distance)
    return min_so_far if min_so_far < float('inf') else -1



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
