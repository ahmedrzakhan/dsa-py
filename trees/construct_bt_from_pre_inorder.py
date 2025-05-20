# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# TC - O(N), SC - O(H)
def buildTree(preorder, inorder):
    # Check if either input array is empty; if so, return None as no tree can be constructed
    if not preorder or not inorder:
        return None

    # Create the root node using the first element of preorder (root comes first in preorder traversal)
    root = TreeNode(preorder[0])

    # Find the index of the root value in the inorder array to split left and right subtrees
    mid = inorder.index(preorder[0])

    # Recursively build the left subtree using:
    # - preorder[1:mid+1]: The left subtree nodes in preorder (after root, up to mid elements)
    # - inorder[:mid]: The left subtree nodes in inorder (before the root)
    root.left = buildTree(preorder[1:mid + 1], inorder[:mid])

    # Recursively build the right subtree using:
    # - preorder[mid+1:]: The right subtree nodes in preorder (after left subtree)
    # - inorder[mid+1:]: The right subtree nodes in inorder (after the root)
    root.right = buildTree(preorder[mid + 1:], inorder[mid + 1:])

    # Return the constructed root node of the current subtree
    return root

# Simple function to print tree in preorder (for verification)
def print_preorder(root):
    if not root:
        return []
    return [root.val] + print_preorder(root.left) + print_preorder(root.right)

# Simple function to print tree in inorder (for verification)
def print_inorder(root):
    if not root:
        return []
    return print_inorder(root.left) + [root.val] + print_inorder(root.right)

# Example 1
preorder1 = [3, 9, 20, 15, 7]
inorder1 = [9, 3, 15, 20, 7]
tree1 = buildTree(preorder1, inorder1)
print(f"Example 1 preorder: {print_preorder(tree1)}")  # Should match preorder1
print(f"Example 1 inorder: {print_inorder(tree1)}")    # Should match inorder1

# Example 2
preorder2 = [-1]
inorder2 = [-1]
tree2 = buildTree(preorder2, inorder2)
print(f"Example 2 preorder: {print_preorder(tree2)}")  # Should be [-1]
print(f"Example 2 inorder: {print_inorder(tree2)}")    # Should be [-1]