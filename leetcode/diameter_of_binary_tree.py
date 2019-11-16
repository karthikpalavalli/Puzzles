# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        def dfs_postorder(node) -> int:
            nonlocal max_diameter

            if node is None:
                return 0

            depth_left = dfs_postorder(node.left)
            depth_right = dfs_postorder(node.right)

            max_diameter = max(max_diameter, depth_right + depth_left)

            return max(depth_left, depth_left) + 1

        max_diameter = 1
        dia_tree = dfs_postorder(root)

        return dia_tree
