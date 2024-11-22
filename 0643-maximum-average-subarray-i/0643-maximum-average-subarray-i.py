class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = sum(nums[0:k])
        currentSum = sum(nums[0:k])
        i = 1
        while i + k <= len(nums):
            currentSum = currentSum - nums[i - 1] + nums[i + k - 1]
            maxSum = max(maxSum, currentSum)
            i += 1
        return maxSum/k