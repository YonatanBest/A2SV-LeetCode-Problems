class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] < 0 and nums[len(nums) - 1] < 0:
            return nums[len(nums) - 1] * nums[len(nums) - 2] * nums[len(nums) - 3]
        if nums[0] * nums[1] > nums[len(nums) - 3] * nums[len(nums) - 2]:
            return nums[0] * nums[1] * nums[len(nums) - 1]
        return nums[len(nums) - 1] * nums[len(nums) - 2] * nums[len(nums) - 3]