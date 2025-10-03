class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(path, i):
            nonlocal ans
            ans.append(path.copy())

            for j in range(i, len(nums)):
                path.append(nums[j])
                backtrack(path, j + 1)
                path.pop()
            
            return
        backtrack([], 0)
        return ans