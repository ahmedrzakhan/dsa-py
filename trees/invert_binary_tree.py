# https://leetcode.com/problems/invert-binary-tree/description/

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# TC - O(N), SC - O(N)
def invertTree( root: TreeNode) -> TreeNode:
    # Base case: if the root is None, return None
    if not root:
        return None

    # Swap the left and right subtrees
    root.left, root.right = root.right, root.left

    # Recursively invert the left subtree
    invertTree(root.left)

    # Recursively invert the right subtree
    invertTree(root.right)

    # Return the root of the inverted tree
    return root

# Example 1: [4,2,7,1,3,6,9]
tree = TreeNode(4,
        TreeNode(2, TreeNode(1), TreeNode(3)),
        TreeNode(7, TreeNode(6), TreeNode(9)))

# Invert and print result
inverted = invertTree(tree)
print(f"Result: root={inverted.val}, left={inverted.left.val}, right={inverted.right.val}")
print(f"Children: {inverted.right.left.val}, {inverted.right.right.val}, {inverted.left.left.val}, {inverted.left.right.val}")