class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s) + 1
        window = [False] * n
        window[0] = True

        for i in range(n):
            for j in range(i):
                if window[j] and s[j:i] in wordDict:
                    window[i] = True
                    break
        return window[-1]