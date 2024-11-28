class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(1, len(nums), 2):
            res += min(nums[i-1], nums[i])
        return res