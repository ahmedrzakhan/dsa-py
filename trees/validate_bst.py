# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# TC - O(N), SC - O(H) where H is the height of the tree
def isValidBST(root) -> bool:
     # Helper function to validate a node within a given range
        def validate(node, min_val, max_val):
            # Base case: an empty node is a valid BST
            if not node:
                return True
            # Check if the current node's value is outside the valid range
            if node.val <= min_val or node.val >= max_val:
                return False
            # Recursively validate left subtree (values < current node's value)
            # and right subtree (values > current node's value)
            return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)

        # Start validation with the root, using -infinity and +infinity as initial bounds
        return validate(root, float('-inf'), float('inf'))

# Example 1: [2,1,3]
#     2
#    / \
#   1   3
tree1 = TreeNode(2,
                TreeNode(1),
                TreeNode(3))

# Example 2: [5,1,4,null,null,3,6]
#     5
#    / \
#   1   4
#      / \
#     3   6
tree2 = TreeNode(5,
                TreeNode(1),
                TreeNode(4,
                        TreeNode(3),
                        TreeNode(6)))

# Test examples
print(f"Example 1: {isValidBST(tree1)}")  # Expected: True
print(f"Example 2: {isValidBST(tree2)}")  # Expected: False

# Additional test case with duplicate values
#     2
#    / \
#   2   3
tree3 = TreeNode(2,
                TreeNode(2),
                TreeNode(3))
print(f"Example 3 (duplicate values): {isValidBST(tree3)}")  # Expected: False