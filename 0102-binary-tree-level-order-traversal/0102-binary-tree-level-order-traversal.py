# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        final_ans = []

        def traverse(root, level):

            if not root:
                return

            if len(final_ans) == level:
                final_ans.append([root.val])
            else:
                final_ans[level].append(root.val)
            
            traverse(root.left, level + 1)
            traverse(root.right, level + 1)

            return
        traverse(root, 0)
        return final_ans
