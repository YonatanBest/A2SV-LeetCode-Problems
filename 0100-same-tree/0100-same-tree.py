# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def traverse(p, q):
            if p and not q:
                return False

            if q and not p:
                return False

            if not q and not p:
                return True

            if p.val != q.val:
                return False
            
            if not traverse(p.left, q.left):
                return False
            if not traverse(p.right, q.right):
                return False
            return True

        return traverse(p, q)