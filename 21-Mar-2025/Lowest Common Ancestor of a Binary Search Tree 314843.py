# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.p_ans = []
        self.q_ans = []
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def steps(check, root, target):
            if root.val == target:
                return check
            if root.val > target:
                check.append("left")
                steps(check, root.left, target)
            if root.val < target:
                check.append("right")
                steps(check, root.right, target)
            return check
        self.p_ans = steps([0], root, p.val)
        self.q_ans = steps([0], root, q.val)
        i = 0
        j = 0
        while i < len(self.p_ans) and j < len(self.q_ans):
            if self.p_ans[i] == self.q_ans[j]:
                if self.p_ans[i] == 0:
                    pass
                elif self.p_ans[i] == "right":
                    root = root.right
                else:
                    root = root.left
            else:
                break
            i += 1
            j += 1
        return root