# Problem: Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root and not root.left and not root.right:
            return [root.val]
        if not root:
            return []
        arr = [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        return arr
