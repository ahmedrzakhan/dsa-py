# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# TC - O(N), SC - O(H)
def kthSmallest(root: TreeNode, k: int) -> int:
    # Counter to keep track of nodes visited
    count = 0
    # Result to store the kth smallest value
    result = None

    def inorder(node):
        nonlocal count, result
        if not node or result is not None:
            return

        # Visit left subtree
        inorder(node.left)

        # Visit current node
        count += 1
        if count == k:
            result = node.val
            return

        # Visit right subtree
        inorder(node.right)

    inorder(root)
    return result

# Example 1: [3,1,4,null,2], k = 1
#     3
#    / \
#   1   4
#    \
#     2
tree1 = TreeNode(3,
                TreeNode(1,
                        None,
                        TreeNode(2)),
                TreeNode(4))
k1 = 1

# Example 2: [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
tree2 = TreeNode(5,
                TreeNode(3,
                        TreeNode(2,
                                TreeNode(1),
                                None),
                        TreeNode(4)),
                TreeNode(6))
k2 = 3

# Create a solution instance

# Test examples
print(f"Example 1: k={k1}, kth smallest = {kthSmallest(tree1, k1)}")  # Expected: 1
print(f"Example 2: k={k2}, kth smallest = {kthSmallest(tree2, k2)}")  # Expected: 3

# Additional test case
#     10
#    /  \
#   5    15
#  / \     \
# 3   7     20
tree3 = TreeNode(10,
                TreeNode(5,
                        TreeNode(3),
                        TreeNode(7)),
                TreeNode(15,
                        None,
                        TreeNode(20)))
k3 = 4
print(f"Example 3: k={k3}, kth smallest = {kthSmallest(tree3, k3)}")  # Expected: 10