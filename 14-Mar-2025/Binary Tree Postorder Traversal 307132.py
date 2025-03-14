# Problem: Binary Tree Postorder Traversal - https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root and not root.left and not root.right:
            return [root.val]
        if not root:
            return []
        arr = self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        return arr