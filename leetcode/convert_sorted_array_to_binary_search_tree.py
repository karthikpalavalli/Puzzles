from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def dfs_inorder_construction(left_ptr, right_ptr):
            if left_ptr > right_ptr:
                return None

            mid = (left_ptr + right_ptr) // 2

            root = TreeNode(nums[mid])
            root.left = dfs_inorder_construction(left_ptr, mid - 1)
            root.right = dfs_inorder_construction(mid + 1, right_ptr)

            return root

        return dfs_inorder_construction(0, len(nums) - 1)