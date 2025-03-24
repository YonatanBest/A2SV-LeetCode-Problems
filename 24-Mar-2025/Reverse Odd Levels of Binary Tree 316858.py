# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def changer(level, tree1, tree2):
            if not tree1:
                return
            if level % 2:
                temp = tree1.val
                tree1.val = tree2.val
                tree2.val = temp
            changer(level + 1, tree1.left, tree2.right)
            changer(level + 1, tree1.right, tree2.left)
        changer(1, root.left, root.right)
        return root