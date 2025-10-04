# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def backtrack(root, ans):
            if root and not root.right and not root.left:
                if ans + root.val == targetSum:
                    return True
                return False
            
            if root.left and backtrack(root.left, ans + root.val):
                return True
            if root.right and backtrack(root.right, ans + root.val):
                return True
            return False
        return backtrack(root, 0)
