class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        total = sum(nums)
        final = int((length*(length + 1))/2 - total)
        return final