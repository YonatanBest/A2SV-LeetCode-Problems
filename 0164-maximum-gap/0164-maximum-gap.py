class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        max_sub = float("-inf")
        for i in range(1, len(nums)):
            max_sub = max(max_sub, nums[i] - nums[i - 1])
        
        return max_sub