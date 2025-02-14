from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = []
        i = 0
        dic = Counter(t)
        window = {}

        def isValid():
            for char in dic:
                if char not in window or dic[char] > window[char]:
                    return False
            return True
        
        for j in range(len(s)):

            if s[j] in window:
                window[s[j]] += 1
            else:
                window[s[j]] = 1

            while isValid():
                if not ans:
                    ans = [i, j]
                if ans[1] - ans[0] > j - i:
                    ans = [i, j]
                    
                window[s[i]] -= 1

                if window[s[i]] == 0:
                    del window[s[i]]
                
                i += 1
        
        if not ans:
            return ""
        return str(s[ans[0]:ans[1] + 1])
