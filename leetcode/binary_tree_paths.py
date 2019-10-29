from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        def build_paths(root, path):
            path += str(root.val)

            if root.left is None and root.right is None:
                paths.append(path)

            else:
                path += "->"
                build_paths(root.left, path)
                build_paths(root.right, path)

        paths = list()
        path = str()

        build_paths(root, path)

        return paths
