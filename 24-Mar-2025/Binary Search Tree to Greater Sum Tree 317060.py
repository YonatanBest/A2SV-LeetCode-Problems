# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(temp, root):
            if not root:
                return temp
            temp = root.val + traverse(temp, root.right)
            root.val = temp
            return traverse(temp, root.left)
        traverse(0, root)
        return root