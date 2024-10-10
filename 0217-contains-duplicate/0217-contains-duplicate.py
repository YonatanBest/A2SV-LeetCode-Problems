class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ans = {}
        for i in nums:
            if i in ans:
                ans[i] += 1
            else:
                ans[i] = 1
        
        
        for i in ans:
            if ans[i] > 1:
                return True
        return False