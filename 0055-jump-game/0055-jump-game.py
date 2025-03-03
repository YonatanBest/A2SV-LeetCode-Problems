class Solution:
    def canJump(self, nums: List[int]) -> bool:
        count = 0
        check = True
        if len(nums) == 1:
            return True
        i = len(nums) - 2
        j = len(nums) - 1
        while i >= 0:
            if j - i <= nums[i]:
                check = True
                j = i
                i -= 1
            else:
                check = False
                i -= 1
            
        return check