class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        result = f'({self.val})'
        next = self.next
        while next:
            result += f'<- ({next.val})'
            next = next.next
        return result


def get_sum(l1, l2):
    carry = 0
    root = n = Node(0)
    while l1 or l2 or carry:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        carry, val = divmod(v1+v2+carry, 10)
        n.next = Node(val)
        n = n.next
    return root.next


if __name__ == '__main__':
    node1 = Node(8)
    node1.next = Node(1)
    node1.next.next = Node(6)
    node2 = Node(5)
    node2.next = Node(9)
    node2.next.next = Node(2)
    sum_node = get_sum(node1, node2)
    print(sum_node)
