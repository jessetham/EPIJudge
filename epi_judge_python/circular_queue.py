from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity):
        self.queue = [0] * capacity
        self.head, self.tail = 0, 0

    def enqueue(self, x):
        self.queue[self.tail] = x
        self.tail += 1
        if self.tail >= len(self.queue):
            self.tail = 0
        if self.tail == self.head:
            old_length = len(self.queue)
            self.queue.extend([0] * old_length)
            for i in range(self.tail, old_length):
                self.queue[old_length+i] = self.queue[i]
            self.head = self.head + old_length

    def dequeue(self):
        if self.head == self.tail:
            raise Exception
        result = self.queue[self.head]
        self.head += 1
        if self.head >= len(self.queue):
            self.head = 0
        return result

    def size(self):
        if self.head <= self.tail:
            size = self.tail - self.head
        else:
            size = (len(self.queue) - self.head) + self.tail
        return size


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure(
                    "Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("circular_queue.py",
                                       'circular_queue.tsv', queue_tester))
