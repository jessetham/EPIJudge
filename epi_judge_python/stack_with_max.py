from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, val):
        if not self.stack:
            self.max_stack.append(val)
        elif val >= self.max_stack[-1]:
            self.max_stack.append(val)
        self.stack.append(val)

    def pop(self):
        if not self.stack:
            return None
        val = self.stack.pop()
        if val == self.max_stack[-1]:
            self.max_stack.pop()
        return val

    def max(self):
        if not self.stack:
            return None
        return self.max_stack[-1]

    def empty(self):
        return len(self.stack) == 0


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("stack_with_max.py",
                                       'stack_with_max.tsv', stack_tester))
