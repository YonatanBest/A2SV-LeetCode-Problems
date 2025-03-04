# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        i = len(nums) - 3
        j = len(nums) - 2
        k = len(nums) - 1
        while i >= 0:
            if nums[i] + nums[j] > nums[k]:
                return nums[i] + nums[j] + nums[k]
            else:
                i -= 1
                j -= 1
                k -= 1
        return 0