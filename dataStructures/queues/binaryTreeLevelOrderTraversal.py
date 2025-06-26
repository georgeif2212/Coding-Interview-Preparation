class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            print("El árbol está vacío.")
            return res

        q = deque()
        q.append(root)
        level_num = 0  # para saber en qué nivel estás

        while q:    
            same_level = []
            level_size = len(q)
            print(f"\n🌱 Nivel {level_num}:")
            print(f"⏳ Cola al inicio del nivel: {[node.val for node in q]}")

            for _ in range(level_size):
                node = q.popleft()
                print(f"👀 Visitando nodo: {node.val}")
                same_level.append(node.val)

                if node.left:
                    print(f"  ↙️ Añadiendo hijo izquierdo: {node.left.val}")
                    q.append(node.left)
                if node.right:
                    print(f"  ↘️ Añadiendo hijo derecho: {node.right.val}")
                    q.append(node.right)

            print(f"✅ Nivel {level_num} completo: {same_level}")
            res.append(same_level)
            level_num += 1

        print("\n🌳 Resultado final por niveles:", res)
        return res


# Creamos un árbol de ejemplo:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

# Ejecutamos la función
sol = Solution()
sol.levelOrder(root)
