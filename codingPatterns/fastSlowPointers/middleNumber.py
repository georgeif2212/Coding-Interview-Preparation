class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def middleNode(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next  
    return slow


# Crear lista: 1 → 2 → 3 → 4 → None
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

middle=middleNode(node1)
print(middle.val)
