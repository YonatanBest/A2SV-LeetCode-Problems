class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                nums[i-1] *= 2
                nums[i] = 0
        zero = 0
        number = 0
        while number < len(nums):
            if nums[number] != 0:
                nums[number], nums[zero] = nums[zero], nums[number]
                zero += 1
            number += 1
        return nums