class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        ones = [0] * len(nums)
        one = n
        for i in range(n - 1, -1, -1):
            if nums[i] == 1:
                one = i

            ones[i] = one
        
        left = 0
        ways = 0
        total = 0
        for right in range(len(nums)):
            total += nums[right]
            while total > goal:
                total -= nums[left]
                left += 1

            if total == goal:
                if goal:
                    ways += ones[left] - left + 1
                else:
                    ways += right - left + 1
        return ways