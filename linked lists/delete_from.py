class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        chain = f'({self.val})'
        next = self.next
        while next:
            chain += f' <- ({next.val})'
            next = next.next
        return chain


def remove_node(node):
    if not node or not node.next:
        return None
    node.val = node.next.val
    node.next = node.next.next


if __name__ == '__main__':
    node = Node(0)
    node.next = Node(1)
    node.next.next = Node(2)
    print(node)
    remove_node(node.next)
    print(node)

