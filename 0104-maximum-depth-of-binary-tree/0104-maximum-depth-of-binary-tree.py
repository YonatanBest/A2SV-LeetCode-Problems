# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        def backtrack(root, level):
            nonlocal max_depth
            if not root:
                max_depth = max(level, max_depth)
                return
            backtrack(root.left, level + 1)
            backtrack(root.right, level + 1)
            return
        backtrack(root, 0)
        return max_depth