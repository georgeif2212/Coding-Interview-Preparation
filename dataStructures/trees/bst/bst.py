class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        def _insert(node, val):
            if not node:
                return TreeNode(val)
            if val < node.val:
                node.left = _insert(node.left, val)
            else:
                node.right = _insert(node.right, val)
            return node

        self.root = _insert(self.root, val)

    def search(self, val):
        def _search(node, val):
            if not node:
                return False
            if node.val == val:
                return True
            elif val < node.val:
                return _search(node.left, val)
            else:
                return _search(node.right, val)

        return _search(self.root, val)

    # ✅ Inorder traversal (devuelve lista en orden)
    def inorder(self):
        res = []

        def _inorder(node):
            if node:
                _inorder(node.left)
                res.append(node.val)
                _inorder(node.right)

        _inorder(self.root)
        return res


def is_valid_bst(node, low=float("-inf"), high=float("inf")):
    if not node:
        return True
    if not (low < node.val < high):
        return False
    return is_valid_bst(node.left, low, node.val) and is_valid_bst(
        node.right, node.val, high
    )


def delete_node(root, key):
    if not root:
        return None
    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        # Buscar el sucesor
        temp = root.right

        while temp.left:
            print(root.val, temp.val)
            temp = temp.left
        root.val = temp.val
        root.right = delete_node(root.right, temp.val)
        print(root.val, root.right.val)
    return root


tree = BST()
for val in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
    tree.insert(val)

# print("Inorder (ordenado):", tree.inorder())  # [1, 3, 4, 6, 7, 8, 10, 13, 14]
# print("Buscar 6:", tree.search(6))  # True
# print("Buscar 2:", tree.search(2))  # False
# print(is_valid_bst(tree.root))

tree2 = BST()
for val in [50, 30, 70, 20, 40, 60, 80]:
    tree2.insert(val)

print("Inorder (ordenado):", tree2.inorder())
print(delete_node(tree2.root, 50).val)
