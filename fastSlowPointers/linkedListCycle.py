# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next  # 1 paso
        fast = fast.next.next  # 2 pasos
        if slow == fast:
            return True
    return False


# Crear lista: 1 → 2 → 3 → 4 → None
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4

print(hasCycle(node1))  # Esperado: False

# Crear lista: 1 → 2 → 3 → 4 → (vuelve a 2)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # 🔁 ciclo aquí


print(hasCycle(node1))  # Esperado: True
