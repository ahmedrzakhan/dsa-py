# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

# TC - O(H), SC - O(1)
def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    # Start from the root node
    curr = root

    while curr:

        # If both p and q are greater than current node,
        # then LCA lies in the right subtree
        if p.val > curr.val and q.val > curr.val:
            curr = curr.right

        # If both p and q are less than current node,
        # then LCA lies in the left subtree

        elif p.val < curr.val and q.val < curr.val:
            curr = curr.left
        # If one is greater and one is less, or one equals the current node,
        # we've found the splitting point, which is the LCA

        else:
            return curr

    return None

# Example 1: [6,2,8,0,4,7,9,null,null,3,5]
#       6
#      / \
#     2   8
#    / \ / \
#   0  4 7  9
#     / \
#    3   5
tree1 = TreeNode(6,
                TreeNode(2,
                        TreeNode(0),
                        TreeNode(4,
                                TreeNode(3),
                                TreeNode(5))),
                TreeNode(8,
                        TreeNode(7),
                        TreeNode(9)))

# Example 2: Same tree as Example 1
# Example 3: [2,1]
tree3 = TreeNode(2, TreeNode(1))

# Test cases
# For Example 1: LCA of 2 and 8
p1, q1 = tree1.left, tree1.right  # Nodes with values 2 and 8
result1 = lowestCommonAncestor(tree1, p1, q1)
print(f"Example 1: LCA of 2 and 8 = {result1.val}")  # Expected: 6

# For Example 2: LCA of 2 and 4
p2, q2 = tree1.left, tree1.left.right  # Nodes with values 2 and 4
result2 = lowestCommonAncestor(tree1, p2, q2)
print(f"Example 2: LCA of 2 and 4 = {result2.val}")  # Expected: 2

# For Example 3: LCA of 2 and 1
p3, q3 = tree3, tree3.left  # Nodes with values 2 and 1
result3 = lowestCommonAncestor(tree3, p3, q3)
print(f"Example 3: LCA of 2 and 1 = {result3.val}")  # Expected: 2