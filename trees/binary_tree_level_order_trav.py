# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# TC - O(N), SC - O(1)
def levelOrder(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.pop(0)
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result

# Example 1: [3,9,20,null,null,15,7]
#      3
#     / \
#    9  20
#      /  \
#     15   7
tree1 = TreeNode(3,
                TreeNode(9),
                TreeNode(20,
                        TreeNode(15),
                        TreeNode(7)))

# Example 2: [1]
tree2 = TreeNode(1)

# Example 3: []
tree3 = None

# Test cases
result1 = levelOrder(tree1)
print(f"Example 1: {result1}")  # Expected: [[3], [9, 20], [15, 7]]

result2 = levelOrder(tree2)
print(f"Example 2: {result2}")  # Expected: [[1]]

result3 = levelOrder(tree3)
print(f"Example 3: {result3}")  # Expected: []