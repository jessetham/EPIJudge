from collections import deque

class MinMaxQueue:
    def __init__(self):
        self.q = deque()
        self.dq = deque()

    def __len__(self):
        return len(self.q)

    def push(self, val):
        while len(self.dq) > 0:
            if self.dq[-1] >= val:
                break
            self.dq.pop()
        self.q.append(val)
        self.dq.append(val)

    def remove(self):
        if len(self.q) == 0:
            raise IndexError
        if self.q[0] == self.dq[0]:
            self.dq.popleft()
        return self.q.popleft()

    def get_max(self):
        if len(self.q) == 0:
            raise IndexError
        return self.dq[0]

    def peek(self):
        if len(self.q) == 0:
            raise IndexError
        return self.q[0]
