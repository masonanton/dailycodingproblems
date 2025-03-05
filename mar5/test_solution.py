import pytest
from mar5.solution import count_unival_subtrees, TreeNode

# Test cases
@pytest.mark.parametrize("root, expected", [
    # Example tree with 5 unival subtrees
    (TreeNode(0, 
        TreeNode(1),
        TreeNode(0, 
            TreeNode(1, 
                TreeNode(1), 
                TreeNode(1)
            ),
            TreeNode(0)
        )
    ), 5),

    # Single node
    (TreeNode(1), 1),

    # Simple tree
    (TreeNode(0, TreeNode(1), TreeNode(2)), 2),

    # All same values
    (TreeNode(1, 
        TreeNode(1, TreeNode(1), TreeNode(1)),
        TreeNode(1)
    ), 5),

    # All leaves are unival
    (TreeNode(2, TreeNode(1), TreeNode(3)), 3),

    # Empty tree
    (None, 0)
])

def test_count_unival_subtrees(root, expected):
    assert count_unival_subtrees(root) == expected
