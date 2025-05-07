# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# TC - O(N), SC - O(H)
def diameterOfBinaryTree(root: TreeNode) -> int:
    diameter = 0

    def dfs(node):
        nonlocal diameter
        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        # Update diameter if path through current node is longer
        diameter = max(diameter, left + right)

        # Return height of current subtree (tree rooted at this node)
        return max(left, right) + 1

    dfs(root)
    return diameter

# Example usage

tree = TreeNode(1,
    TreeNode(2, TreeNode(4), TreeNode(5)),
    TreeNode(3))

print(f"Diameter: {diameterOfBinaryTree(tree)}")  # Expected: 3

# Example 2: [1,2]
tree2 = TreeNode(1, TreeNode(2))
print(f"Diameter: {diameterOfBinaryTree(tree2)}")  # Expected: 1