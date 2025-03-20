class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.min_diff = float("inf")

        def backtrack(path, i):
            if path and max(path) > self.min_diff and self.min_diff != float("inf"):
                return
            if len(cookies) == i:
                self.min_diff = min(max(path), self.min_diff)
                return
            for j in range(k):
                path[j] += cookies[i]
                backtrack(path, i + 1)
                path[j] -= cookies[i]       
        backtrack([0]*k, 0)
        return self.min_diff