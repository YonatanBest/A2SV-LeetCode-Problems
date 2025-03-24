# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        self.ans = []
        def zigzag(level, root):
            if not root:
                return
            if len(self.ans) < level + 1:
                self.ans.append([root.val])
            else:
                self.ans[level].append(root.val)

            zigzag(level + 1, root.left)
            zigzag(level + 1, root.right)
        zigzag(0, root)
        for i in range(len(self.ans)):
            if i % 2:
                self.ans[i] = list(reversed(self.ans[i]))
        return self.ans
            
            