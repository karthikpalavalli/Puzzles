from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = list()

        result_list = list()

        if root is None:
            return result_list

        queue.append(root)
        result_list.append(queue)
        flag = True

        while queue:
            next_queue = list()

            for node in queue:
                if node.left:
                    next_queue.append(node.left)

                if node.right:
                    next_queue.append(node.right)

            queue = next_queue

            if flag:
                next_queue.reverse()

            result_list.append([node.val for node in next_queue])
            flag = not flag

        return result_list
