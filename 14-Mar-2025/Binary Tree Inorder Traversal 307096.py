# Problem: Binary Tree Inorder Traversal - https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root and not root.left and not root.right:
            return [root.val]
        if not root:
            return []
        arr = self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        return arr