class StackNode:

    def __init__(self, val, prev):
        self.val = val
        self.prev = prev

    def __repr__(self):
        return f'Node {self.val}, ({self.prev})'


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.top = StackNode(float('inf'), None)
        self.min = float('inf')

    def push(self, x: int) -> None:
        if self.top.val == float('inf'):
            self.min = x
        if x < self.min:
            old_min = self.min
            self.min = x
            x = 2 * x - old_min
        self.top = StackNode(x, self.top)

    def pop(self) -> None:
        if self.top.val < self.min:
            self.min = 2 * self.min - self.top.val
        self.top = self.top.prev

    def top(self) -> int:
        if self.top.val < self.min:
            return self.min
        return self.top.val

    def getMin(self) -> int:
        return int(self.min)


if __name__ == '__main__':
    # minStack = MinStack()
    # minStack.push(-2)
    # minStack.push(0)
    # minStack.push(-3)
    # print(minStack.getMin())
    # minStack.pop()
    # minStack.push(-4)
    # minStack.push(9)
    # print(minStack.getMin())
    # print(minStack.top())
    # print(minStack.getMin())
    min_stack = MinStack()
    min_stack.push(0)
    min_stack.push(-2)
    min_stack.push(3)
    min_stack.pop()
    min_stack.pop()
    min_stack.pop()
    min_stack.push(-99)
    print(min_stack.getMin())

