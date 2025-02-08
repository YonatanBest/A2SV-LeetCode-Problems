class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            index = (nums[i] + i) % len(nums)
            result[i] = nums[index]
        return result