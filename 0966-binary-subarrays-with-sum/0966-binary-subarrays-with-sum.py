class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        def atmost(nums, goal):
            left = answer = total = 0
            n = len(nums)
            for right in range(n):
                total += nums[right]
                while total > goal:
                    total -= nums[left]
                    left += 1
                
                answer += right - left + 1
            
            return answer

        if goal:
            return atmost(nums, goal) - atmost(nums, goal - 1)

        return atmost(nums, goal)