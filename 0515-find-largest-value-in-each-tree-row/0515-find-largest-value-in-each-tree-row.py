# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
        self.level = []
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        def finder(num, root):
            if not root:
                return
            if len(self.level) <= num:
                self.level.append([root.val])
            else:
                self.level[num].append(root.val)
            finder(num + 1, root.right)
            finder(num + 1, root.left)
        finder(0, root)
        for arr in self.level:
            self.ans.append(max(arr))
        return self.ans