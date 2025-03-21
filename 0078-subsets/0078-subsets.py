class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(i, path):
            ans.append(path.copy())
            if i == len(nums):
                return
            for j in range(i, len(nums)):
                path.append(nums[j])
                backtrack(j + 1, path)
                path.pop()
            return
        backtrack(0, [])
        return ans