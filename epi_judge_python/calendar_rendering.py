import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A):
    if not A:
        return 0
    times = []
    for event in A:
        times.append(Event(event.start, False))
        times.append(Event(event.finish, True))
    times.sort()

    max_consecutive_so_far, num_consecutive = 0, 0
    for time in times:
        if time.finish: # This is an endtime
            num_consecutive -= 1
        else: # This is a starttime
            num_consecutive += 1
            max_consecutive_so_far = max(max_consecutive_so_far,
                num_consecutive)
    return max_consecutive_so_far


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(
        functools.partial(find_max_simultaneous_events, events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("calendar_rendering.py",
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
