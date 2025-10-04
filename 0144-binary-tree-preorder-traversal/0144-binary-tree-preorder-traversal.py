# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        path = []
        def backtrack(root):
            nonlocal path
            if not root:
                return
            path.append(root.val)
            backtrack(root.left)
            backtrack(root.right)
            return
        backtrack(root)
        return path
        