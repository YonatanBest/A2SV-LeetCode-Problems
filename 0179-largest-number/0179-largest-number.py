class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if int(str(nums[j - 1]) + str(nums[j])) < int(str(nums[j]) + str(nums[j - 1])):
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
        ans = ""
        for k in nums:
            ans += str(k)
        ans = str(int(ans))
        return ans