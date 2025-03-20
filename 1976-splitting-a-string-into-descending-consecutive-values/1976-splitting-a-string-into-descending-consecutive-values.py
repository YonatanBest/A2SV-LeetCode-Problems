class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(i, path):
            if len(s) == i:
                for k in range(1, len(path)):
                    if path[k] + 1 != path[k - 1]:
                        return False
                return len(path) >= 2
            num = 0
            for j in range(i, len(s)):
                num = num*10 + int(s[j])
                path.append(num)
                if backtrack(j + 1, path):
                    return True
                path.pop()
            return False
        ans = backtrack(0, [])
        return ans