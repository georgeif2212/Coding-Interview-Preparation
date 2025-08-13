class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    prevNode = None
    curr = head
    while curr:
        nextNode = curr.next  # temporal para almacenar el siguiente nodo
        curr.next = prevNode  # conecta al nodo previo
        prevNode = curr  # Esta linea sirve para indicar que el actual será el nuevo previo
        curr = nextNode  # Esta linea sirve para iterar al siguiente nodo
    return prevNode # En prev se queda el último node, en curr queda el none


def printList(head):
    while head:
        print(head.val, end="->")
        head = head.next
    print("None")


# Crear manualmente una lista
n4 = ListNode(4)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)


def inorder(node):
    if node:
        inorder(node.left)
        print(node)
        inorder(node.right)


print(reverse_list(n1))
printList(n4)
