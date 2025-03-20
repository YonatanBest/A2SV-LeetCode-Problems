import itertools
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.min_diff = float("inf")
        all = set()
        for permutation in itertools.permutations(cookies):
            all.add(permutation)
        all = list(all)
        self.total = sum(cookies)
        for cook in all:
            def backtrack(i, path):
                if len(cookies) == i:
                    temp = max(path)
                    if len(path) == k and self.total == sum(path):
                        self.min_diff = min(temp, self.min_diff)
                    return
                
                num = 0
                for j in range(i, len(cookies)):
                    if num + cook[j] > self.min_diff:
                        continue
                    num = num + cook[j]
                    path.append(num)
                    backtrack(j + 1, path)
                    path.pop()
                return 
            backtrack(0, [])
        return self.min_diff