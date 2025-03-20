class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.min_diff = float("inf")

        def backtrack(path, i):
            if len(cookies) == i:
                self.min_diff = min(max(path), self.min_diff)
                return
            for j in range(k):
                if path[j] + cookies[i] > self.min_diff:
                    continue
                path[j] += cookies[i]
                backtrack(path, i + 1)
                path[j] -= cookies[i]       
        backtrack([0]*k, 0)
        return self.min_diff