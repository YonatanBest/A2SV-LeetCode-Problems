class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(i, path, used):
            if len(path) == len(nums):
                ans.append(path.copy())
                return
            for j in range(len(nums)):
                if nums[j] in used:
                    continue
                path.append(nums[j])
                used.add(nums[j])
                backtrack(i + 1, path, used)
                used.remove(path.pop())

            return ans
        return backtrack(0, [], set())