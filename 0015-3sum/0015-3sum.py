class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        k = len(nums) - 1
        ans = set()
        while k >= 2:
            i = 0
            j = k - 1
            while i < j:
                if nums[i] + nums[j] + nums[k] > 0:
                    j -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    i += 1
                else:
                    ans.add((nums[i], nums[j], nums[k]))
                    j -= 1
            k -= 1
        return list(ans)