# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dic = {}
        for i in range(len(nums)):
            dic[i] = nums[i]
        for j in range(len(nums)):
            nums[(j + k) % len(nums)] = dic[j]
        return nums