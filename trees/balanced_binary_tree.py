# https://leetcode.com/problems/balanced-binary-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# TC - O(N), SC - O(H)
def isBalanced(root: TreeNode) -> bool:
    # Return (is_balanced, height)
    def dfs(node):
        # Base case: empty node has height 0 and is balanced
        if not node:
            return True, 0

        # Check if left subtree is balanced and get its height
        left_balanced, left_height = dfs(node.left)
        if not left_balanced:
            return False, 0  # Early return if left subtree is unbalanced

        # Check if right subtree is balanced and get its height
        right_balanced, right_height = dfs(node.right)
        if not right_balanced:
            return False, 0  # Early return if right subtree is unbalanced

        # Check if current node is balanced
        is_balanced = abs(left_height - right_height) <= 1

        # Return if the tree is balanced and its height
        return is_balanced, max(left_height, right_height) + 1

    # Start DFS from root and return only the is_balanced result
    balanced, _ = dfs(root)
    return balanced

# Example 1: [3,9,20,null,null,15,7]
#    3
#   / \
#  9  20
#    /  \
#   15   7
tree1 = TreeNode(3,
                TreeNode(9),
                TreeNode(20,
                        TreeNode(15),
                        TreeNode(7)))

# Example 2: [1,2,2,3,3,null,null,4,4]
#     1
#    / \
#   2   2
#  / \
# 3   3
#/ \
#4 4
tree2 = TreeNode(1,
                TreeNode(2,
                        TreeNode(3,
                                TreeNode(4),
                                TreeNode(4)),
                        TreeNode(3)),
                TreeNode(2))

# Example 3: []
tree3 = None

# Test all examples
print(f"Example 1: {isBalanced(tree1)}")  # Expected: True
print(f"Example 2: {isBalanced(tree2)}")  # Expected: False
print(f"Example 3: {isBalanced(tree3)}")  # Expected: True