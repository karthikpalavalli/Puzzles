class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        return self.helper(root.left, root.right)

    def helper(self, node_left, node_right) -> bool:
        if node_left is None and node_right is None:
            return True

        elif node_left is None or node_right is None:
            return False

        elif node_left.val == node_right.val and self.helper(node_left.left, node_right.right) \
                and self.helper(node_left.right, node_right.left):
            return True

        return False
