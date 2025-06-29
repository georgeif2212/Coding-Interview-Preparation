class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1  # cabeza de la lista


def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


def reverse_list(head):
    # 🧱 Caso base: si está vacía o es el último nodo
    if not head or not head.next:
        return head

    # 🔁 Invertimos recursivamente el resto de la lista
    new_head = reverse_list(head.next)

    # 🔄 Reconexión: el siguiente nodo apunta hacia atrás
    head.next.next = head
    head.next = None

    # 🎯 Devolvemos el nuevo head al final de la recursión
    return new_head


print_list(head)
newHead = reverse_list(head)
print_list(newHead)


# [4, 3, 2, 1]
# [4, 3],[2, 1]
# [3, 4, 1, 2]
