# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = sum(nums[:k])
        cur_sum = max_sum
        for i in range(k, len(nums)):
            cur_sum -= nums[i - k]
            cur_sum += nums[i]
            max_sum = max(cur_sum, max_sum)
        return max_sum / k