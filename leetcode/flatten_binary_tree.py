class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def traverse_to_rightmost(node_val):
    while node_val.left is not None and node_val.right is not None:
        node_val = node_val.right
    return node_val


def flatten(root):
    left_branch_checker = root
    right_leaf = root

    right_leaf = traverse_to_rightmost(right_leaf)

    while left_branch_checker.right is not None and left_branch_checker.left is not None:
        if left_branch_checker.left is not None:
            right_leaf.right = left_branch_checker.left
            right_leaf = traverse_to_rightmost(right_leaf)
            


