# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# TC - O(N), SC - O(H) where H is the height of the tree
def maxDepth(root: TreeNode) -> int:
    # Base case: if the root is None, return 0
    if not root:
        return 0

    # Recursively find the depth of left and right subtrees
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)

    # Return the maximum depth plus 1 for the current node
    return max(left_depth, right_depth) + 1

# Example 1: [3,9,20,null,null,15,7]
tree = TreeNode(3,
        TreeNode(9),
        TreeNode(20, TreeNode(15), TreeNode(7)))

# Calculate and print the maximum depth
depth = maxDepth(tree)
print(f"Maximum depth of the tree: {depth}")  # Should output 3

# Example 2: [1,null,2]
tree2 = TreeNode(1,
        None,
        TreeNode(2))

# Calculate and print the maximum depth
depth2 = maxDepth(tree2)
print(f"Maximum depth of the second tree: {depth2}")  # Should output 2