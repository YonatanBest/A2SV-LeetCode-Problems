# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        curr = 0
        queue = deque([[root,0]])
        check = True
        while queue:
            root, curr = queue.popleft()
            if root:
                if root.left:
                    queue.append([root.left, curr + 1])
                if root.right:
                    queue.append([root.right, curr + 1])
            if curr + 1 > len(ans):
                ans.append([root.val])
            else:
                ans[curr].append(root.val)
        return ans