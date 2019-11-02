class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def dfs_inorder(root):
            if root is None:
                return

            nonlocal list_form

            dfs_inorder(root.left)

            list_form.append(root.val)

            dfs_inorder(root.right)

        list_form = list()

        dfs_inorder(root)

        for idx in range(0, len(list_form) - 1):
            if list_form[idx + 1] < list_form[idx]:
                return False

        return True
