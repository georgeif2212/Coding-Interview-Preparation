class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node8 = TreeNode(8)
node7 = TreeNode(7)
node6 = TreeNode(6)
node5 = TreeNode(5)
node4 = TreeNode(4, None, node8)
node3 = TreeNode(3, node6, node7)
node2 = TreeNode(2, node4)
node1 = TreeNode(1, node3, node5)


node0 = TreeNode(0, node1, node2)
