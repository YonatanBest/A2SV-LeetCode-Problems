class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(i, path):
            if sum(path) > target:
                return

            if sum(path) == target:
                ans.append(path.copy())
                return

            for j in range(len(candidates)):
                path.append(candidates[j])
                backtrack(i + 1, path)
                path.pop()
            return

        backtrack(0, [])
        new = set()
        for k in ans:
            new.add(tuple(sorted(k)))
        return list(new)