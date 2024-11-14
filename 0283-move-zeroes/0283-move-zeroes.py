class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0
        number = 0
        while number < len(nums):
            if nums[zero] == 0 and nums[number] != 0:
                nums[zero], nums[number] =  nums[number], nums[zero]
                zero += 1
                number += 1
            elif nums[zero] == 0 and nums[number] == 0:
                number += 1
            else:
                zero += 1
                number += 1
        return nums           