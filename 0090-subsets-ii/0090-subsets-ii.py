class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(i, path):
            ans.append(tuple(path.copy()))
            if i == len(nums):
                return
            for j in range(i, len(nums)):
                path.append(nums[j])
                backtrack(j + 1, path)
                path.pop()
            return
        backtrack(0, [])
        new = []
        test = set()
        for k in ans:
            temp = tuple(sorted(k))
            if temp not in test:
                new.append(k)
                test.add(temp)
        return new