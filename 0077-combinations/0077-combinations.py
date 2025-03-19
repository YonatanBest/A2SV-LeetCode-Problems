class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(firstNum, path):
            if len(path) == k:
                ans.append(path[:])
                return 

            for can in range(firstNum, n + 1):
                path.append(can)
                backtrack(can + 1, path)
                path.pop()
        backtrack(1, [])
        return ans