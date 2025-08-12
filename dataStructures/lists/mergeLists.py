class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printList(head):
    while head:
        print(head.val, end="->")
        head = head.next
    print("None")


def merge_lists(l1, l2):
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 or l2
    return dummy.next


# Crear manualmente una lista
n4 = ListNode(4)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

n5 = ListNode(8)
n6 = ListNode(7, n5)
n7 = ListNode(9, n6)
n8 = ListNode(0, n7)

nx = merge_lists(n1, n8)

printList(nx)
