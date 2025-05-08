# https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# TC - O(N), SC - O(H) where N is number of nodes and H is height of tree
def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    # If both nodes are None, they are the same
    if not p and not q:
        return True

    # If one node is None but the other isn't, they are different
    if not p or not q:
        return False

    # Check if current nodes have same value
    # AND left subtrees are the same
    # AND right subtrees are the same
    return (p.val == q.val and
            isSameTree(p.left, q.left) and
            isSameTree(p.right, q.right))

# Example 1: p = [1,2,3], q = [1,2,3]
#   1       1
#  / \     / \
# 2   3   2   3
p1 = TreeNode(1, TreeNode(2), TreeNode(3))
q1 = TreeNode(1, TreeNode(2), TreeNode(3))

# Example 2: p = [1,2], q = [1,null,2]
#   1       1
#  /         \
# 2           2
p2 = TreeNode(1, TreeNode(2), None)
q2 = TreeNode(1, None, TreeNode(2))

# Example 3: p = [1,2,1], q = [1,1,2]
#   1       1
#  / \     / \
# 2   1   1   2
p3 = TreeNode(1, TreeNode(2), TreeNode(1))
q3 = TreeNode(1, TreeNode(1), TreeNode(2))

# Test all examples
print(f"Example 1: {isSameTree(p1, q1)}")  # Expected: True
print(f"Example 2: {isSameTree(p2, q2)}")  # Expected: False
print(f"Example 3: {isSameTree(p3, q3)}")  # Expected: False