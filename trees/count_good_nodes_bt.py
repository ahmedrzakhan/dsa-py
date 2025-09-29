# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# TC - O(N), SC - O(H) where H is the height of the tree
def goodNodes(root: TreeNode) -> int:
    count = 0
    def dfs(node, max_so_far):
        nonlocal count
        # Base case: reached end of branch
        if not node:
            return None

        # Check if current node is "good"
        # It's good if it's >= all values we've seen on the path
        if node.val >= max_so_far:
            count += 1

        # Update the highest value for the next level
        max_so_far = max(max_so_far, node.val)

        # Explore left and right branches
        dfs(node.left, max_so_far)
        dfs(node.right, max_so_far)

    dfs(root, float('-inf'))
    return count

# Example 1: [3,1,4,3,null,1,5]
#     3
#    / \
#   5   4
#  /   / \
# 3   1   5
tree1 = TreeNode(3,
                TreeNode(5,
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

# Example 4: [5,4,6,1,5,null,7,3,null,null,null,4,8]
#        5
#       / \
#      4   6
#     / \   \
#    1   5   7
#   /       / \
#  3       4   8
tree4 = TreeNode(5,
                TreeNode(4,
                        TreeNode(1,
                                TreeNode(3),
                                None),
                        TreeNode(5)),
                TreeNode(6,
                        None,
                        TreeNode(7,
                                TreeNode(4),
                                TreeNode(8))))
print(f"Example 4: {goodNodes(tree4)}")  # Expected: 5

# Example 5: [10,5,15,1,8,12,20,null,2]
#        10
#       /  \
#      5    15
#     / \   / \
#    1   8 12  20
#     \
#      2
tree5 = TreeNode(10,
                TreeNode(5,
                        TreeNode(1,
                                None,
                                TreeNode(2)),
                        TreeNode(8)),
                TreeNode(15,
                        TreeNode(12),
                        TreeNode(20)))

print(f"\nExample 5: {goodNodes(tree5)}")  # Expected: 7
