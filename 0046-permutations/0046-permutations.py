class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(i, path):
            if len(set(path)) != len(path):
                return
            if len(path) == len(nums):
                ans.append(path.copy())
                return
            if i == len(nums):
                return
            for j in range(len(nums)):
                path.append(nums[j])
                backtrack(i + 1, path)
                path.pop()
            return
        backtrack(0, [])
        return ans