
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    root = temp = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            temp.next = l1
            l1 = l1.next
        else:
            temp.next = l2
            l2 = l2.next
        temp = temp.next # перевод указателя
    temp.next = l1 or l2
    return root.next


if __name__ == '__main__':
    result1 = mergeTwoLists([1, 2, 4], [1, 3, 4])
