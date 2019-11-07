from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

        def bfs_inorder(root):
            nonlocal right_view
            current_queue = list()
            next_queue = list()

            current_queue.append(root)

            while current_queue:

                for node in current_queue:
                    if node.left:
                        next_queue.append(node.left)
                    if node.right:
                        next_queue.append(node.right)

                if next_queue:
                    right_view.append(next_queue[-1].val)

                current_queue = next_queue
                next_queue = list()

        right_view = list()

        if not root:
            return []

        right_view.append(root.val)
        bfs_inorder(root)

        return right_view
