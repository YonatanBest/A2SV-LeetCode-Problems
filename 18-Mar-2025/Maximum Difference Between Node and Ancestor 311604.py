# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_dif = float("-inf")

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def deep_copy_tree(root):
            if root is None:
                return None
            new_node = TreeNode(root.val)
            new_node.left = deep_copy_tree(root.left)
            new_node.right = deep_copy_tree(root.right)
            return new_node

        temp = deep_copy_tree(root)

        def difByMin(root):
            if not root:
                return

            if root.right:
                self.max_dif = max(self.max_dif, abs(root.val - root.right.val))
            if root.left:
                self.max_dif = max(self.max_dif, abs(root.val - root.left.val))

            if root.right and root.val < root.right.val:
                root.right.val = root.val
            if root.left and root.val < root.left.val:
                root.left.val = root.val

            difByMin(root.left)
            difByMin(root.right)

        def difByMax(root):
            if not root:
                return
            if root.right:
                self.max_dif = max(self.max_dif, abs(root.val - root.right.val))
            if root.left:
                self.max_dif = max(self.max_dif, abs(root.val - root.left.val))
            if root.right and root.val > root.right.val:
                root.right.val = root.val
            if root.left and root.val > root.left.val:
                root.left.val = root.val

            difByMax(root.left)
            difByMax(root.right)

        difByMin(temp)
        difByMax(root)
        return self.max_dif
        
        
        