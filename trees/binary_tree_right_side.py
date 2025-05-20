# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# TC - O(N), SC - O(H) where H is the height of the tree
def rightSideView(root: TreeNode) -> list[int]:
    result = []

    # Helper function for DFS traversal
    def dfs(node, level):
        if not node:
            return

        # If this is the first node we're seeing at this level
        # It will be the rightmost when we visit right first
        # When the level equals the current length of the result list,
        # it means this is the first (and rightmost) node seen at this level
        if level == len(result):
            result.append(node.val)

        # Visit right subtree first, then left
        # This ensures we encounter the rightmost node of each level first
        dfs(node.right, level + 1)
        dfs(node.left, level + 1)

    dfs(root, 0)
    return result

# Example 1: [1,2,3,null,5,null,4]
#     1
#    / \
#   2   3
#    \   \
#     5   4
tree1 = TreeNode(1,
                 TreeNode(2,
                         None,
                         TreeNode(5)),
                 TreeNode(3,
                         None,
                         TreeNode(4)))

# Example 2: [1,2,3,4,null,null,null,5]
#      1
#     / \
#    2   3
#   /
#  4
# /
#5
tree2 = TreeNode(1,
                 TreeNode(2,
                         TreeNode(4,
                                 TreeNode(5),
                                 None),
                         None),
                 TreeNode(3))

# Example 3: [1,null,3]
#  1
#   \
#    3
tree3 = TreeNode(1, None, TreeNode(3))

# Example 4: []
tree4 = None

# Test all examples
print(f"Example 1: {rightSideView(tree1)}")  # Expected: [1,3,4]
print(f"Example 2: {rightSideView(tree2)}")  # Expected: [1,3,4,5]
print(f"Example 3: {rightSideView(tree3)}")  # Expected: [1,3]
print(f"Example 4: {rightSideView(tree4)}")  # Expected: []