class MaxStack(list):
    def push(self, x):
        max_val = max(x, self[-1][1] if self else None)
        self.append((x, max_val))

    def pop(self):
        return list.pop(self)[0]

    def top(self):
        return self[-1][0] if self else None

    def peekMax(self):
        return self[-1][1] if self else None

    def popMax(self):
        max_val = self[-1][1]
        buffer = []
        while self[-1][0] != max_val:
            buffer.append(self.pop())

        self.pop()
        map(self.push, reversed(buffer))
        return max_val
