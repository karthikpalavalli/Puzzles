# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        def dfs_inorder(node_p, node_q):
            nonlocal same_tree
            if node_p is None and node_q is None:
                return

            if node_p is None or node_q is None:
                same_tree = False
                return

            dfs_inorder(node_p.left, node_q.left)

            if node_p.val != node_q.val:
                same_tree = False

            dfs_inorder(node_p.right, node_q.right)

        same_tree = True

        dfs_inorder(p, q)

        return same_tree

