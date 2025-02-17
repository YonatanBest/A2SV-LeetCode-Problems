class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        currSum = 0

        for i in range(len(nums)):
            total -= nums[i]
            if currSum == total:
                return i
            currSum += nums[i]
        return -1
