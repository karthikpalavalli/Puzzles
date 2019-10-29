class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        current_queue = list()
        next_queue = list()

        if not root:
            return 0

        else:
            depth = 0

            current_queue.append(root)

            while current_queue:
                curr_node = current_queue.pop(0)

                if curr_node.left:
                    next_queue.append(curr_node.left)

                if curr_node.right:
                    next_queue.append(curr_node.right)

                if not current_queue:
                    depth += 1
                    current_queue = next_queue
                    next_queue = list()

        return depth
