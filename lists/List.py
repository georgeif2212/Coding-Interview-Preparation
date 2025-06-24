class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printList(head):
    while head:
        print(head.val, end="->")
        head = head.next
    print("None")


def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nextNode = curr.next  # temporal para almacenar el siguiente nodo
        curr.next = prev  # conecta al nodo previo
        prev = curr  # Esta linea sirve para indicar que el actual será el nuevo previo
        curr = nextNode  # Esta linea sirve para iterar al siguiente nodo
    return prev


def removeNode(head, value):
    dummy = ListNode(0)
    dummy.next = head
    curr = dummy

    while curr and curr.next:
        if curr.next.val == value:
            curr.next = curr.next.next  # * Elimina el nodo conectando al siguiente siguiente
            break  # si solo quieres eliminar una vez
        curr = curr.next

    return dummy.next


# Crear manualmente una lista
n4 = ListNode(4)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

printList(n1)
removeNode(n1, 2)
printList(n1)
print(reverse_list(n1))
print(n3)
printList(n4)
