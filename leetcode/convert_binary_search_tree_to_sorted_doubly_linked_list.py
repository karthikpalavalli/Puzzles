# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs_inorder(root):
            nonlocal previous, head

            if root is None:
                return

            dfs_inorder(root.left)

            if previous is None:
                head = root

            else:
                root.left = previous
                previous.right = root

            previous = root

            dfs_inorder(root.right)

        head = None
        previous = None

        if root is not None:
            dfs_inorder(root)

            previous.right = head
            head.left = previous

        return head

