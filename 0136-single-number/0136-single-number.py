class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        for j in nums:
            x ^= j
        return x