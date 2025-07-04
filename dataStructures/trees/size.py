class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Construimos este árbol:
#         1
#        / \
#       2   3
#      / \
#     4   5

# Crear nodos
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


def size(root):
    if not root:
        return 0
    return 1 + size(root.left) + size(root.right)


print(size(root))
