class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_str = [0, 0]  
        for x in range(0, len(s) - 1):
            mid = x
            i = mid - 1
            j = mid + 1
            string = [x, x]
            while i >= 0 and j < len(s):
                if s[i] != s[j]:
                    break
                max_str = [i, j] if max_str[1] - max_str[0] < j - i else max_str
                i -= 1
                j += 1

            if x + 1 >= len(s) or s[x] != s[x + 1]:
                continue
            i = x
            j = x + 1
            max_str = [i, j] if max_str[1] - max_str[0] < j - i else max_str
            i -= 1
            j += 1
            while i >= 0 and j < len(s):
                if s[i] != s[j]:
                    break
                max_str = [i, j] if max_str[1] - max_str[0] < j - i else max_str
                i -= 1
                j += 1
        return s[max_str[0]:max_str[1] + 1]