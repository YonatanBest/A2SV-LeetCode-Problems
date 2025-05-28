class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        for j in range(len(nums)):
            ans[j] = nums[nums[j]]
        return ans