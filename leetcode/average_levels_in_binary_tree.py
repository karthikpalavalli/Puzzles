from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []

        current_nodes = list()
        next_nodes = list()

        current_nodes.append(root)
        result_level_sum = list()

        while current_nodes:
            level_sum = 0

            for curr_node in current_nodes:
                if curr_node.left:
                    next_nodes.append(curr_node.left)

                if curr_node.right:
                    next_nodes.append(curr_node.right)

                level_sum += curr_node.val

            result_level_sum.append(level_sum / len(current_nodes))
            current_nodes = next_nodes
            next_nodes = list()

        return result_level_sum
