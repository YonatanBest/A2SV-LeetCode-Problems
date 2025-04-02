# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        mid = (i + j)//2
        while i <= j:
            if nums[mid] == mid:
                i = mid + 1
            else:
                j = mid - 1
            mid = (i + j)//2
        return i