# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        path = []
        def backtrack(root):
            nonlocal path
            
            if not root:
                return

            backtrack(root.left)
            backtrack(root.right)
            path.append(root.val)

            return
        backtrack(root)
        return path