# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = []
        def num(root):
            if root and not root.left and not root.right:
                self.ans.append(root.val)
            if not root:
                return
            if root.left:
                root.left.val = root.left.val + root.val*10
            if root.right:
                root.right.val = root.right.val + root.val*10
            num(root.left)
            num(root.right)
        num(root)
        return sum(self.ans)
