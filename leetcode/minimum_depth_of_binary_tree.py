# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:

        def bfs_levelorder(node) -> int:
            if node is None:
                return 0

            depth = 1
            current_queue = [node]
            next_queue = list()

            while current_queue:
                depth = depth + 1

                for curr_node in current_queue:
                    if curr_node.left is None and curr_node.right is None:
                        return depth

                    if curr_node.left:
                        next_queue.append(curr_node.left)

                    if curr_node.right:
                        next_queue.append(curr_node.right)

                current_queue = next_queue
                next_queue = list()

        return bfs_levelorder(root)
