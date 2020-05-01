class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, val):
        if not self.last:
            self.last = Node(val)
            self.first = self.last
        else:
            self.last.next = Node(val)
            self.last = self.last.next

    def remove(self):
        if not self.first:
            raise IndexError('Queue is empty. Nothing to remove.')
        self.first = self.first.next
        if not self.first:
            self.last = None

    def peek(self):
        if not self.first:
            raise IndexError('Queue is empty. Nothing to peek.')
        return self.first.val

    def is_empty(self):
        return self.first is None


if __name__ == '__main__':
    queue = Queue()
    print(queue.is_empty())
    queue.add(1)
    print(queue.is_empty())
    queue.add(2)
    queue.peek()
    queue.remove()
    queue.remove()
    print(queue.is_empty())
