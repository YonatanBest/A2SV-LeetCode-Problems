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
        
        final_ans = []

        queue = deque([root])
        
        while queue:

            for i in range(len(queue)):

                node = queue.popleft()

                if i == 0:
                    final_ans.append([node.val])
                else:
                    final_ans[len(final_ans) - 1].append(node.val)
                
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return final_ans
