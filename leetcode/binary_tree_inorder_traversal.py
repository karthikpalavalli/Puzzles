class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        node_stack = list()
        result_list = list()

        if root is None:
            return result_list

        node = root

        while True:
            if node is not None:
                node_stack.append(node)
                node = node.left

            else:
                if not node_stack:
                    break

                node = node_stack.pop()
                result_list.append(node.val)
                node = node.right

        return result_list
