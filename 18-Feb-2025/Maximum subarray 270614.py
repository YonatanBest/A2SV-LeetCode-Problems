# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        answer = float("-inf")
        for num in nums:
            total += num
            answer = max(answer, total)
            total = max(total, 0)

        return answer