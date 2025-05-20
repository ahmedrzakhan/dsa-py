# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# TC - O(N), SC - O(H) where H is the height of the tree
def goodNodes(root: TreeNode) -> int:
    def dfs(node, max_so_far):
        if not node:
            return 0

        # Count current node as good if its value is >= max seen so far
        count = 1 if node.val >= max_so_far else 0

        # Update max value for children
        max_so_far = max(max_so_far, node.val)

        # Add counts from left and right subtrees
        count += dfs(node.left, max_so_far)
        count += dfs(node.right, max_so_far)

        return count

    return dfs(root, float('-inf'))

# Example 1: [3,1,4,3,null,1,5]
#     3
#    / \
#   1   4
#  /   / \
# 3   1   5
tree1 = TreeNode(3,
                TreeNode(1,
                        TreeNode(3),
                        None),
                TreeNode(4,
                        TreeNode(1),
                        TreeNode(5)))

# Example 2: [3,3,null,4,2]
#     3
#    /
#   3
#  / \
# 4   2
tree2 = TreeNode(3,
                TreeNode(3,
                        TreeNode(4),
                        TreeNode(2)),
                None)

# Example 3: [1]
#  1
tree3 = TreeNode(1)

# Test all examples
print(f"Example 1: {goodNodes(tree1)}")  # Expected: 4
print(f"Example 2: {goodNodes(tree2)}")  # Expected: 3
print(f"Example 3: {goodNodes(tree3)}")  # Expected: 1