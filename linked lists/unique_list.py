# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        result = ''
        s = self
        while s:
            result += str(s.val) + '->'
            s = s.next
        return result[:-2]


def deleteDuplicates(head: ListNode) -> ListNode:
    root = temp = ListNode(0)
    while head.next:
        if head.val != head.next.val:
            temp.next = head
            temp = temp.next
        head = head.next
    temp.next = head
    return root.next


if __name__ == '__main__':
    a = ListNode(1)
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(3)
    a4 = ListNode(3)
    a.next = a1
    a1.next = a2
    a2.next = a3
    a3.next = a4
    result1 = deleteDuplicates(a)
    print(result1)
