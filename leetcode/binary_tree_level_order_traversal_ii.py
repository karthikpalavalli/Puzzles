from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        def bfs_traversal():
            nonlocal result_list

            if root is None:
                return

            queue = list()
            next_queue = list()

            queue.append(root)
            result_list.append([root.val])

            while queue:

                for node in queue:
                    if node.left:
                        next_queue.append(node.left)

                    if node.right:
                        next_queue.append(node.right)

                result_list = [next_queue] + result_list

                queue = next_queue
                next_queue = list()

        result_list = list()
        bfs_traversal()

        return result_list
