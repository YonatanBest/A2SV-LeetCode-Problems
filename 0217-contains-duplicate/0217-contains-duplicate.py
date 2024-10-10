class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ans = {}
        for i in nums:
            if i in ans:
                return True
            else:
                ans[i] = 1
        return False