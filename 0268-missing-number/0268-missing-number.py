class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return nums[-1] + 1