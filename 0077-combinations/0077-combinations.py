class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(firstNum, path):
            if len(path) == k:
                ans.append(path[:])
                return 
            if firstNum > n:
                return
            path.append(firstNum)
            backtrack(firstNum + 1, path)
            path.pop()
            backtrack(firstNum + 1, path)
        backtrack(1, [])
        return ans