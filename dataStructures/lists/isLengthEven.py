class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isLengthEven(head):
    def _islengthEven(head):
        if head is None:
            return 0
        return 1 + _islengthEven(head.next)

    counter = _islengthEven(head)
    print(counter)
    return True if counter % 2 == 0 else False


def isLengthEven(head):
    toggle = True
    while head:
        toggle = not toggle
        head = head.next
    return toggle


# Crear manualmente una lista
n4 = ListNode(4)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

# printList(n1)
print(isLengthEven(n1))
