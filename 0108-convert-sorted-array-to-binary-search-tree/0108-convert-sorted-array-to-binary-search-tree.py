# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        self.tree = TreeNode()
        def recursion(tree, nums):
            if len(nums) == 0:
                return
            
            right = TreeNode()
            left = TreeNode()

            tree.val = nums[len(nums)//2]

            if len(nums[len(nums)//2 + 1:]) > 0:
                tree.right = right
            
            if len(nums[:len(nums)//2]) > 0:
                tree.left = left

            recursion(right, nums[len(nums)//2 + 1:])
            recursion(left, nums[:len(nums)//2])
    
        recursion(self.tree, nums)

        return self.tree