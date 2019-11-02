class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        def dfs_inorder(root):
            if root is None:
                return

            nonlocal closest_value

            dfs_inorder(root.left)

            if (root.val - target) ** 2 < (closest_value - target) ** 2:
                closest_value = root.val

            dfs_inorder(root.right)

        closest_value = 10 ** 5

        dfs_inorder(root)

        return closest_value
