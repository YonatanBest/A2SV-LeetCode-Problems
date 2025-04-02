class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_num = max(nums)
        return (len(nums)*(len(nums) + 1))//2 - sum(nums)
