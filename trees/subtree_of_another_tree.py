# https://leetcode.com/problems/subtree-of-another-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# TC - O(M*N), SC - O(H)
def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    return (p.val == q.val and
            isSameTree(p.left, q.left) and
            isSameTree(p.right, q.right))

def isSubtree(root: TreeNode, subRoot: TreeNode) -> bool:
    if not subRoot:
        return True
    if not root:
        return False
    if isSameTree(root, subRoot):
        return True
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)

# Example 1
root1 = TreeNode(3,
                TreeNode(4, TreeNode(1), TreeNode(2)),
                TreeNode(5))
subRoot1 = TreeNode(4, TreeNode(1), TreeNode(2))

# Example 2
root2 = TreeNode(3,
                TreeNode(4,
                        TreeNode(1),
                        TreeNode(2, TreeNode(0), None)),
                TreeNode(5))
subRoot2 = TreeNode(4, TreeNode(1), TreeNode(2))

# Test examples
print(f"Example 1: {isSubtree(root1, subRoot1)}")  # Expected: True
print(f"Example 2: {isSubtree(root2, subRoot2)}")  # Expected: False