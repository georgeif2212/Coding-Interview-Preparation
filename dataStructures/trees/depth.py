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
root.left.left.left = TreeNode(6)


def depth(root, target, current_depth=0):
    if not root:
        return -1
    if root.val == target:
        return current_depth
    left = depth(root.left, target, current_depth + 1)
    if left != -1:
        return left
    return depth(root.right, target, current_depth + 1)


print(depth(root, 6))
