class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def count_unival_subtrees(root: TreeNode) -> int:
    # base cases (none or leaf)
    from typing import Tuple

    def helper(node: TreeNode) -> Tuple[int, bool]:
        if not node: # empty node
            return 0, True
        if not node.left and not node.right: # leaf node
            return 1, True
        # recursive case
        left_count, is_left_unival = helper(node.left)
        right_count, is_right_unival = helper(node.right)
        total_count = left_count + right_count
        if is_left_unival and is_right_unival:
            if node.left and node.left.val != node.val:
                return total_count, False
            if node.right and node.right.val != node.val:
                return total_count, False
            return total_count + 1, True
        return total_count, False
    return helper(root)[0]
    
        