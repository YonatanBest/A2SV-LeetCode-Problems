# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        visited = set([root.val])
        queue = deque([root])
        while queue:
            if len(visited) > 1:
                return False
            if root:
                if root.left:
                    visited.add(root.left.val)
                    queue.append(root.left)
                if root.right:
                    visited.add(root.right.val)
                    queue.append(root.right)
            root = queue.popleft()
        return True