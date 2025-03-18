# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
            if root and not root.left and not root.right:
                self.ans += root.val
            if not root:
                return 
            if root.left:
                root.left.val = root.left.val + root.val*10
            if root.right:
                root.right.val = root.right.val + root.val*10
            self.sumNumbers(root.left)
            self.sumNumbers(root.right)
            return self.ans
