# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def dfs(node):
            nonlocal min_val
            nonlocal second_min

            if not node:
                return

            dfs(node.left)

            if node.val < second_min and node.val != min_val:
                second_min = node.val

            dfs(node.right)

        min_val = root.val
        second_min = float("inf")

        dfs(root)

        if second_min == float("inf"):
            second_min = -1

        return second_min
