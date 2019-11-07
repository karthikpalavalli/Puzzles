from typing import List
from collections import defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

        def dfs_preorder(root, distance, depth):
            if root is None:
                return

            nonlocal level_dict

            level_dict[(distance, depth)].append(root.val)

            dfs_preorder(root.left, distance - 1, depth + 1)
            dfs_preorder(root.right, distance + 1, depth + 1)

        level_dict = defaultdict(list)

        dfs_preorder(root, 0, 0)
        result_list = list()

        x_list = sorted([key[0] for key, value in level_dict.items()])
        y_list = sorted([key[1] for key, value in level_dict.items()])

        for x in x_list:
            temp_list = list()

            for y in y_list:
                temp_list.extend(sorted(level_dict[(x, y)]))

            result_list += temp_list

        return result_list

