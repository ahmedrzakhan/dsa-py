# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # TC - O(N), SC - O(H)
    def maxPathSum(self, root: TreeNode) -> int:
        max_sum = float('-inf')

        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0

            # Ensuring non-negative contributions
            left_sum = max(dfs(node.left), 0)
            right_sum = max(dfs(node.right), 0)

            curr_sum = node.val + left_sum + right_sum

            max_sum = max(max_sum, curr_sum)

            return node.val + max(left_sum, right_sum)

        dfs(root)
        return max_sum


# Test cases
def test():
    sol = Solution()

    # Example 1: root = [1,2,3]
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    print(f"Example 1: {sol.maxPathSum(root1)}")  # Expected: 6

    # Example 2: root = [-10,9,20,null,null,15,7]
    root2 = TreeNode(-10)
    root2.left = TreeNode(9)
    root2.right = TreeNode(20)
    root2.right.left = TreeNode(15)
    root2.right.right = TreeNode(7)
    print(f"Example 2: {sol.maxPathSum(root2)}")  # Expected: 42

    # Example 3: Single node with negative value
    root3 = TreeNode(-3)
    print(f"Example 3: {sol.maxPathSum(root3)}")  # Expected: -3

    # Example 4: All negative values
    root4 = TreeNode(-1)
    root4.left = TreeNode(-2)
    root4.right = TreeNode(-3)
    print(f"Example 4: {sol.maxPathSum(root4)}")  # Expected: -1

test()